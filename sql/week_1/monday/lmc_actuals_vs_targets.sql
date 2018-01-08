select 
		# pull the required fields
		Coalesce(IF(F1.Product IS NULL, concat('<b>',F1.`Group`,' Total</b>'),F1.`group`),'<b>&#127;Grand Total</b>') AS `Group`,
		Coalesce(IF(F1.LeadSource IS NULL, concat('<b>',F1.Product,' Total</b>'),F1.product),'') AS Product,
		Coalesce(IF(F1.CampaignName IS NULL, concat('<b>',F1.LeadSource,' Total</b>'),F1.LeadSource),'') AS LeadSource,
		Coalesce(IF(F1.Campaignname IS NULL, concat('<b>',F1.Campaignname,' Total</b>'),F1.CampaignName),'') AS CampaignName,

		date_format(F1.CreateTime, "%Y-%m-%d") as 'Date',
		
		# -- Liam said Shannon wanted the Vendor field to show up as well...?
		#F1.Vendor as 'Vendor',

		# use that as Target
		coalesce(F4.Target, 0) as 'Target',

		# count guid(s) in combined  - use this as received
		count(F1.data_lead_guid) as 'Received',

		# calculate the shortfall
		greatest(0,((coalesce(F4.Target, 0)) - (coalesce(count(F1.data_lead_guid), 0)))) as 'Shortfall'

from
		(

				select 
						F2.data_lead_guid,
						coalesce(F3.`Group`, "") as 'Group',
						F2.Campaign as 'Campaignname',
						F2.Product,
						F2.LeadSource,
						F2.CreateTime as 'CreateTime',
						F2.data_lead_guid as 'Received'


						from `reach.axion`.bloom_reach_combined as F2

								left join `lmc.axion`.data_campaign_routing as F3
								on F2.Campaign = F3.Campaign

								left join `reach.axion`.data_campaign_targets as F5
								on F2.Campaign = F5.Campaign
		) as F1

left join `lmc.axion`.data_campaign_targets as F4
on F1.Campaignname = F4.Campaign and date_format(F1.createTime, "%Y%m") = F4.`Date`

# group the data
group by F1.`Group`, F1.Product, F1.LeadSource, F1.campaignname, F1.createTime with rollup

having
		#valid results
		(F1.`group` is not null and F1.product is not null and F1.Leadsource is not null and F1.Campaignname is not null AND F1.CampaignName is not null and F1.CreateTime is not null)

		# keep grand total
		OR (F1.`group` is null and F1.product is null and F1.leadsource is null and F1.Campaignname is null and F1.campaignname is null and F1.createtime is null)

		# keep sub totals, excluding createtime
		OR (F1.campaignname is null and F1.createtime is null)
		AND F1.`group` <> ''

