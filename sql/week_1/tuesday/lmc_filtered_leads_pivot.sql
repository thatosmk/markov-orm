select 

		# prepare your headers
		concat('{LeadSource:\"',coalesce(LeadSource,'None'),'",') AS 'LeadSource',
		concat('Date:\"',coalesce(DATE(`CreateTime`),'None'),'",') AS 'Date',
		concat('CampaignName:\"',coalesce(CampaignName,'None'),'",') AS 'CampaignName', 
		concat('Product:\"',coalesce(Product,'None'),'",') AS 'Product', 
		concat('InboundCampaignCode:\"',coalesce(Campaign,'None'),'",') AS 'InboundCampaignCode', 
		concat('OutboundCampaignCode:\"',coalesce(OutboundCampaign,'None'),'",') AS 'OutboundCampaignCode', 
		concat('Callcenter:\"',coalesce(Callcenter,'None'),'"},')

from


(
		select 
				Campaign,`Cell`,
				min(CreateTime) as `CreateTime`,
				Product,
				LeadSource,
				OutboundCampaign,
				Callcenter,
				CampaignName 

			from
				(
						select 
								A.Campaign,
								msisdn as `Cell`,
								CreateTime,
								R.Product,
								R.LeadSource,
								R.OutboundCampaign,
								R.Callcenter,
								R.CampaignName 

								from `losuat.axion`.`bloom_loslead_data_lead` as A 
								
								left join `lmc.axion`.`data_campaign_routing` as R 
								# this is the same as A.campaign = R.campaign
								on A.Campaign like R.Campaign

								union all
								select 
									A.Campaign,
									if(msisdn LIKE '',mobile,msisdn) as `Cell`,
										CreateTime,
										R.Product,
										R.LeadSource,
										R.OutboundCampaign,
										R.Callcenter,
										R.CampaignName 

										from `lmc.axion`.`bloom_loslead_data_lead` as A 
										left join `lmc.axion`.`data_campaign_routing` as R ON A.Campaign LIKE R.Campaign) as Dataset
										WHERE Product LIKE 'LIFE'
										GROUP BY Cell) AS PvtData


		union all



		SELECT 

		concat('{LeadSource:\"',coalesce(LeadSource,'None'),'",') AS 'LeadSource',
		concat('Date:\"',coalesce(DATE(`CreateTime`),'None'),'",') AS 'Date',
		concat('CampaignName:\"',coalesce(CampaignName,'None'),'",') AS 'CampaignName', 
		concat('Product:\"',coalesce(Product,'None'),'",') AS 'Product', 
		concat('InboundCampaignCode:\"',coalesce(Campaign,'None'),'",') AS 'InboundCampaignCode', 
		concat('OutboundCampaignCode:\"',coalesce(OutboundCampaign,'None'),'",') AS 'OutboundCampaignCode', 
		concat('Callcenter:\"',coalesce(Callcenter,'None'),'"},')

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

		concat('{LeadSource:\"',coalesce(LeadSource,'None'),'",') AS 'LeadSource',
		concat('Date:\"',coalesce(DATE(`CreateTime`),'None'),'",') AS 'Date',
		concat('CampaignName:\"',coalesce(CampaignName,'None'),'",') AS 'CampaignName', 
		concat('Product:\"',coalesce(Product,'None'),'",') AS 'Product', 
		concat('InboundCampaignCode:\"',coalesce(Campaign,'None'),'",') AS 'InboundCampaignCode', 
		concat('OutboundCampaignCode:\"',coalesce(OutboundCampaign,'None'),'",') AS 'OutboundCampaignCode', 
		concat('Callcenter:\"',coalesce(Callcenter,'None'),'"},')

		FROM


		(SELECT Campaign,`Cell`,min(CreateTime) AS `CreateTime`,Product,LeadSource,OutboundCampaign,Callcenter,CampaignName FROM
				(SELECT A.Campaign,msisdn AS `Cell`,CreateTime,R.Product,R.LeadSource,R.OutboundCampaign,R.Callcenter,R.CampaignName FROM `losuat.axion`.`bloom_loslead_data_lead` AS A LEFT JOIN `lmc.axion`.`data_campaign_routing` AS R ON 
						A.Campaign LIKE R.Campaign
						UNION ALL
						SELECT A.Campaign,IF(msisdn LIKE '',mobile,msisdn) AS `Cell`,CreateTime,R.Product,R.LeadSource,R.OutboundCampaign,R.Callcenter,R.CampaignName FROM `lmc.axion`.`bloom_loslead_data_lead` AS A LEFT JOIN `lmc.axion`.`data_campaign_routing` AS R ON A.Campaign LIKE R.Campaign) AS Dataset
				WHERE Product LIKE 'FUNERAL'
				GROUP BY Cell) AS PvtData;
