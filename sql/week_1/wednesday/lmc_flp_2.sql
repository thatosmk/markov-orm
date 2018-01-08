SELECT 

CONCAT('{LeadSource:\"',coalesce(LeadSource,'None'),'",') AS 'LeadSource',
CONCAT('Date:\"',coalesce(DATE(`CreateTime`),'None'),'",') AS 'Date',
CONCAT('CampaignName:\"',coalesce(CampaignName,'None'),'",') AS 'CampaignName', 
CONCAT('Product:\"',coalesce(Product,'None'),'",') AS 'Product', 
CONCAT('InboundCampaignCode:\"',coalesce(Campaign,'None'),'",') AS 'InboundCampaignCode', 
CONCAT('OutboundCampaignCode:\"',coalesce(OutboundCampaign,'None'),'",') AS 'OutboundCampaignCode', 
CONCAT('Callcenter:\"',coalesce(Callcenter,'None'),'"},')

FROM


(SELECT Campaign,`Cell`,min(CreateTime) AS `CreateTime`,Product,LeadSource,OutboundCampaign,Callcenter,CampaignName FROM
		(SELECT A.Campaign,msisdn AS `Cell`,CreateTime,R.Product,R.LeadSource,R.OutboundCampaign,R.Callcenter,R.CampaignName FROM `losuat.axion`.`bloom_loslead_data_lead` AS A LEFT JOIN `lmc.axion`.`data_campaign_routing` AS R ON 
				A.Campaign LIKE R.Campaign
				UNION ALL
				SELECT A.Campaign,IF(msisdn LIKE '',mobile,msisdn) AS `Cell`,CreateTime,R.Product,R.LeadSource,R.OutboundCampaign,R.Callcenter,R.CampaignName FROM `lmc.axion`.`bloom_loslead_data_lead` AS A LEFT JOIN `lmc.axion`.`data_campaign_routing` AS R ON A.Campaign LIKE R.Campaign) AS Dataset
		WHERE Product LIKE 'LIFE'
		GROUP BY Cell) AS PvtData


UNION ALL



SELECT 

CONCAT('{LeadSource:\"',coalesce(LeadSource,'None'),'",') AS 'LeadSource',
CONCAT('Date:\"',coalesce(DATE(`CreateTime`),'None'),'",') AS 'Date',
CONCAT('CampaignName:\"',coalesce(CampaignName,'None'),'",') AS 'CampaignName', 
CONCAT('Product:\"',coalesce(Product,'None'),'",') AS 'Product', 
CONCAT('InboundCampaignCode:\"',coalesce(Campaign,'None'),'",') AS 'InboundCampaignCode', 
CONCAT('OutboundCampaignCode:\"',coalesce(OutboundCampaign,'None'),'",') AS 'OutboundCampaignCode', 
CONCAT('Callcenter:\"',coalesce(Callcenter,'None'),'"},')

FROM


(SELECT Campaign,`Cell`,min(CreateTime) AS `CreateTime`,Product,LeadSource,OutboundCampaign,Callcenter,CampaignName FROM
		(SELECT A.Campaign,msisdn AS `Cell`,CreateTime,R.Product,R.LeadSource,R.OutboundCampaign,R.Callcenter,R.CampaignName FROM `losuat.axion`.`bloom_loslead_data_lead` AS A LEFT JOIN `lmc.axion`.`data_campaign_routing` AS R ON 
				A.Campaign LIKE R.Campaign
				UNION ALL
				SELECT A.Campaign,IF(msisdn LIKE '',mobile,msisdn) AS `Cell`,CreateTime,R.Product,R.LeadSource,R.OutboundCampaign,R.Callcenter,R.CampaignName FROM `lmc.axion`.`bloom_loslead_data_lead` AS A LEFT JOIN `lmc.axion`.`data_campaign_routing` AS R ON A.Campaign LIKE R.Campaign) AS Dataset
		WHERE Product LIKE 'CAR'
		GROUP BY Cell) AS PvtData



UNION ALL


SELECT 

CONCAT('{LeadSource:\"',coalesce(LeadSource,'None'),'",') AS 'LeadSource',
CONCAT('Date:\"',coalesce(DATE(`CreateTime`),'None'),'",') AS 'Date',
CONCAT('CampaignName:\"',coalesce(CampaignName,'None'),'",') AS 'CampaignName', 
CONCAT('Product:\"',coalesce(Product,'None'),'",') AS 'Product', 
CONCAT('InboundCampaignCode:\"',coalesce(Campaign,'None'),'",') AS 'InboundCampaignCode', 
CONCAT('OutboundCampaignCode:\"',coalesce(OutboundCampaign,'None'),'",') AS 'OutboundCampaignCode', 
CONCAT('Callcenter:\"',coalesce(Callcenter,'None'),'"},')

FROM


(SELECT Campaign,`Cell`,min(CreateTime) AS `CreateTime`,Product,LeadSource,OutboundCampaign,Callcenter,CampaignName FROM
		(SELECT A.Campaign,msisdn AS `Cell`,CreateTime,R.Product,R.LeadSource,R.OutboundCampaign,R.Callcenter,R.CampaignName FROM `losuat.axion`.`bloom_loslead_data_lead` AS A LEFT JOIN `lmc.axion`.`data_campaign_routing` AS R ON 
				A.Campaign LIKE R.Campaign
				UNION ALL
				SELECT A.Campaign,IF(msisdn LIKE '',mobile,msisdn) AS `Cell`,CreateTime,R.Product,R.LeadSource,R.OutboundCampaign,R.Callcenter,R.CampaignName FROM `lmc.axion`.`bloom_loslead_data_lead` AS A LEFT JOIN `lmc.axion`.`data_campaign_routing` AS R ON A.Campaign LIKE R.Campaign) AS Dataset
		WHERE Product LIKE 'FUNERAL'
		GROUP BY Cell) AS PvtData;
