select
        # pull the required fields
        coalesce(F2.`Group`, '') as 'Group',
		coalesce(F1.Product, '') as 'Product',
		F1.LeadSource as 'Leadsource',
		F1.Campaign as 'Campaignname',
		F1.UpdateTime as 'Date',
		F1.Vendor as 'Vendor',

		# use that as Target
		coalesce(F4.Target, 0) as 'Target',

		# count guid(s) in combined  - use this as received
		count(F1.data_lead_guid) as 'Received',

		# calculate the shortfall
		greatest(0,((coalesce(F4.Target, 0)) - (coalesce(count(F1.data_lead_guid), 0)))) as 'Shortfall'

		# select table
		from `reach.axion`.bloom_reach_combined as F1 

left join `lmc.axion`.data_campaign_routing as F2
on F1.Campaign = F2.Campaign 

# find the target
left join `lmc.axion`.data_campaign_targets as F4
on F1.Campaign = F4.Campaign

left join `reach.axion`.data_campaign_targets as F5
on F1.Campaign = F5.Campaign

# group by Product from bloom_reach_combined
group by F1.Product, F2.`Group`, F1.Leadsource 

# keep valid results
having (F2.`Group` is not null and F1.Product is not null and F1.Leadsource is not null)

# final bit will be to just put a 'where' clause on the date for filtering

