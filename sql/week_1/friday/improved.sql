select A.Product, A.Campaign, coalesce(B.Target, 0) as 'Target', count(*)
from `reach.axion`.bloom_reach_combined A
left join `lmc.axion`.data_campaign_targets B
on A.Campaign = B.Campaign and date_format(B.CreateTime, "%Y%m") = A.CreateTime
group by A.Campaign
order by Target desc
