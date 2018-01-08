SELECT 

CONCAT('{LeadSource:\"',coalesce(LeadSource,'None'),'",') AS 'LeadSource',
CONCAT('Date:\"',coalesce(DATE(`CreateTime`),'None'),'",') AS 'Date',
CONCAT('Product:\"',coalesce(Product,'None'),'",') AS 'Product', 
CONCAT('InboundCampaignCode:\"',coalesce(InboundCampaign,'None'),'",') AS 'InboundCampaignCode', 
CONCAT('Callcenter:\"',coalesce(Callcenter,'None'),'"},')

FROM
	`xx_playground`.adm_reach_feedback

/* let me know if the column names are okay */

