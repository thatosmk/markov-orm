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
