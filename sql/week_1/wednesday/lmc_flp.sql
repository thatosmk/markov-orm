# the first part -- 'Life' section

select 
		# prepare your headers
		concat('{LeadSource:\"',coalesce(LeadSource,'None'),'",') AS 'LeadSource',
		concat('Date:\"',coalesce(DATE(`CreateTime`),'None'),'",') AS 'Date',
		concat('CampaignName:\"',coalesce(CampaignName,'None'),'",') AS 'CampaignName', 
		concat('Product:\"',coalesce(Product,'None'),'",') AS 'Product', 
		concat('InboundCampaignCode:\"',coalesce(Campaign,'None'),'",') AS 'InboundCampaignCode', 
		concat('OutboundCampaignCode:\"',coalesce(OutboundCampaign,'None'),'",') AS 'OutboundCampaignCode', 
		concat('Callcenter:\"',coalesce(Callcenter,'None'),'"},') as 'Callcenter'

from
(
		select
			F5.Campaign,
			F5.`Cell`,
			F5.Product,
			F5.LeadSource,
			F5.OutboundCampaign,
			F5.Callcenter,
			F5.CampaignName

			from
			(
				select 
					F2.Campaign as 'Campaign',
					F2.Msisdn as `Cell`,
					F2.CreateTime,
					F3.Product,
					F3.LeadSource,
					F3.OutboundCampaign,
					F3.Callcenter,
					F3.CampaignName

				from `losuat.axion`.bloom_loslead_data_lead as F2

				left join `lmc.axion`.data_campaign_routing as F3
				on F2.campaign = F3.campaign

				# also join with another table
				union all
				select
					F3.Campaign,
					if(Msisdn like '',mobile, msisdn) as `Cell`,				
					CreateTime,
					F4.Product,
					F4.LeadSource,
					F4.OutboundCampaign,
					F4.Product,
					F4.Callcenter,
					F4.CampaignName

				from `lmc.axion`.bloom_loslead_data_lead as F3
				left join `lmc.axion`.data_campaign_routing as F4
				on F3.Campaign = F4.Campaign) as Dataset
			    where Product like 'LIFE'
				group by `Cell`
) as PvtData


# the second part -- 'Car' section

union all

select

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
		Campaign,
		`Cell`,
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
			B.Product,
			B.LeadSource,
			B.OutboundCampaign,
			B.Callcenter,
			B.CampaignName
		from 
			`losuat.axion`.bloom_loslead_data_lead as A
		left join `lmc.axion`.data_campaign_routing as B
		on A.Campaign = B.Campaign

		union all

		select
			A.Campaign,
			if(msisdn like '', mobile, msisdn) as `Cell`,
			CreateTime,
			B.Product,
			B.LeadSource,
			B.OutboundCampaign,
			B.Callcenter,
			B.CampaignName
		from
			`lmc.axion`.bloom_loslead_data_lead as A
	    left join `lmc.axion`.data_campaign_routing as B
		on A.Campaign = B.Campaign
	) as Dataset
	where Product like 'CAR'
	group by `Cell`
) as PvtData


union all

select

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
		Campaign,
		`Cell`,
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
			B.Product,
			B.LeadSource,
			B.OutboundCampaign,
			B.Callcenter,
			B.CampaignName
		from 
			`losuat.axion`.bloom_loslead_data_lead as A
		left join `lmc.axion`.data_campaign_routing as B
		on A.Campaign = B.Campaign

		union all

		select
			A.Campaign,
			if(msisdn like '', mobile, msisdn) as `Cell`,
			CreateTime,
			B.Product,
			B.LeadSource,
			B.OutboundCampaign,
			B.Callcenter,
			B.CampaignName
		from
			`lmc.axion`.bloom_loslead_data_lead as A
	    left join `lmc.axion`.data_campaign_routing as B
		on A.Campaign = B.Campaign
	) as Dataset
	where Product like 'FUNERAL'
	group by `Cell`
) as PvtData
