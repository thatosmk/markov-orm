/* below is the given table and need to pull data from it */
SELECT *
FROM
(
		SELECT
		    F1.data_lead_guid AS `Guid`,
		    F4.campaign AS `InboundCampaign`, 
			/* get the most up-to-date time */
		    (F1.createtime) AS `Createtime`,
		    F4.Product,
		    F4.LeadSource,
		    F4.Callcenter,
		    F4.`Group`,
		    F1.First_Name,
		    F1.Mobile AS Mobile,
		    F3.Definition,
		    F2.AttemptDT AS `Attempt DATE`
		   
		FROM

		(SELECT data_lead_guid, your_var,Campaign,CreateTime,RDG1,Mobile,First_Name FROM
				    `lmc.axion`.bloom_loslead_data_lead)  AS F1
		    
		LEFT JOIN 
		    
		(SELECT LeadReference,max(LeadAttemptDT) AS `AttemptDT`,CallOutcome FROM `lmc.axion`.bloom_occ_feedback_new GROUP BY LeadReference
				UNION
				SELECT RefNo_LeadID,max(attempt_date_and_time),CallOutcome FROM `lmc.axion`.bloom_msa_feedback_new GROUP BY RefNo_leadID) AS F2

		ON F1.data_lead_guid = F2.LeadReference

		LEFT JOIN

		`xx_playground`.results_key AS F3
		ON F2.CallOutcome = F3.Code

		LEFT JOIN `lmc.axion`.data_campaign_routing AS F4
		ON F4.Campaign = F1.Campaign
		    

		GROUP BY F1.data_lead_guid
) AS F6
/* join with reach data */
union 
(
		select *
		from `xx_playground`.adm_lmc_feedback  
)as R

/* pull only the latest data from adm_reach */
/*group by F6.LeadSource, F6.Product, F6.Createtime, F6.CallCenter, F6.Mobile, F6.`Attempt Date`, F6.`Group`, F6.InboundCampaign with rollup
*/
having
(F6.`Guid` is not null and F6.Product is not null and F6.LeadSource is not null and F6.InboundCampaign is not null AND F6.CreateTime is not null and F6.Callcenter is not null and F6.`Group` is not null and F6.First_Name is not null and F6.Mobile is not null and F6.Definition is not null and F6.`Attempt DATE` is not null )

