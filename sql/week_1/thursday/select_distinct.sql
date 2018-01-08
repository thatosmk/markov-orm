select distinct *
from
(
select Product, Vendor, date_format(`Date`,"%Y-%m-%d") as `Date`, Target from
(
select coalesce(A.Product, '') as 'Product',A.Vendor, A.CreateTime as `Date`, A.Campaign, A.LeadSource, 
coalesce(B.Target,0) as 'Target'
 from `lmc.axion`.bloom_loslead_data_lead as A
left join `lmc.axion`.data_campaign_targets as B
on A.Campaign = B.Campaign
group by A.Campaign
) pvt
) pvtr
having `Date` like "2017-10-24"