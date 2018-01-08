select 
	Coalesce(IF(A.Product IS NULL, concat('<b>',A.`Group`,' Total</b>'),A.`group`),'<b>&#127;Grand Total</b>') AS `Group`,
	Coalesce(IF(A.LeadSource IS NULL, concat('<b>',A.Product,' Total</b>'),A.product),'') AS Product,
	Coalesce(IF(A.Campaign IS NULL, concat('<b>',A.LeadSource,' Total</b>'),A.LeadSource),'') AS LeadSource,
	Coalesce(B.Target, 0) as Target

from 
(
select

)
`lmc.axion`.data_campaign_routing as A

left join `lmc.axion`.data_campaign_targets as B
on A.Campaign = B.Campaign

group by `Group`, Product, LeadSource

having

(`group` is not null and product is not null and Leadsource is not null )

OR (`group` is null and product is null and leadsource is null )

AND `group` <> ''



