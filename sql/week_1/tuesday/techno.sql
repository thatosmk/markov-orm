select 
    Product, 
    CampaignCode, 
    bloom_loslead_data_leadUpdateTime 

from 
    `lmc.axion`.bloom_reach_combined  as F1 

#inner join bloom_reach_routing as F2 on bloom_reach_combined.Product = bloom_reach_routing.Product;
