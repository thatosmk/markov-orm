select 
	concat('{LeadSource:\"', coalesce(LeadSource, 'None'), '",') as 'LeadSource',
	concat('{Product:\"', coalesce(Product, 'None'), '",') as 'Product'

from 
(
		select 
			A.LeadSource,
			A.Product
		from
			`lmc.axion`.bloom_loslead_data_lead as A
		left join `lmc.axion`.data_campaign_routing as B
		on A.Campaign =  B.Campaign

		group by A.Product
) pvt

group by LeadSource
