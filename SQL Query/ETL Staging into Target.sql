INSERT INTO [D_BusRoute] (
	[id], 
	[stop],
	[service], 
	[direction],
	[seq],  
	[dist]
	)
SELECT [id],  
right('000000000000'+ rtrim(case stop when 'null' then null else stop end), 5) as stop, /*Left pad with 0 to 5 digits*/
[service], 
[direction],
[seq],  
[dist]
FROM [STAGING_BusStops];
GO
PRINT 'D_BusRoute populated'

INSERT INTO [D_BusStops] (
		[id]
      ,[stop]
      ,[description]
      ,[road]
      ,[station]
      ,[lng]
      ,[lat]
      ,[x]
      ,[y]
	)
SELECT distinct [id] 
	  ,right('000000000000'+ rtrim(case stop when 'null' then null else stop end), 5) as stop /*Left pad with 0 to 5 digits*/
      ,[description]
      ,[road]
      ,[station]
      ,[lng]
      ,[lat]
      ,[x]
      ,[y]
FROM [STAGING_BusStops];
GO
PRINT 'D_BusStop populated'

insert into F_Service
			([src]
           ,[dst]
           ,[hr]
           ,[min]
           ,[km]
           ,[pax]
		   ,[dayofweek])
SELECT right('000000000000'+ rtrim(case src when 'null' then null else src end), 5) as src /*Left pad with 0 to 5 digits*/
      ,right('000000000000'+ rtrim(case dst when 'null' then null else dst end), 5) as dst
	  ,cast(hr as int) as hr
      ,cast(min as decimal(18,4)) as min
      ,cast(km as decimal(18,4)) as km
	  ,cast(replace(pax, CHAR(13), '') as int) as pax  /*Remove carriage return character*/
	  ,'WEEKDAY'
FROM [transport].[dbo].[STAGING_12Weekday] 
GO
PRINT 'F_Service (Weekday) populated'

insert into F_Service
			([src]
           ,[dst]
           ,[hr]
           ,[min]
           ,[km]
           ,[pax]
		   ,[dayofweek])
SELECT right('000000000000'+ rtrim(case src when 'null' then null else src end), 5) as src /*Left pad with 0 to 5 digits*/
      ,right('000000000000'+ rtrim(case dst when 'null' then null else dst end), 5) as dst
	  ,cast(hr as int) as hr
      ,cast(min as decimal(18,4)) as min
      ,cast(km as decimal(18,4)) as km
	  ,cast(replace(pax, CHAR(13), '') as int) as pax  /*Remove carriage return character*/
	  ,'SUNDAY'
FROM [transport].[dbo].[STAGING_12Sun] 
GO
PRINT 'F_Service (Sun) populated'

/*delete from staging_d_busstops
delete from staging_f_sunday
delete from staging_f_weekday

delete from f_service
delete from d_busstops*/

/* Old Schema
INSERT INTO [D_BusRoute] (
	[id], 
	[stop],
	[service], 
	[direction],
	[seq], 
	[description], 
	[road], 
	[station] , 
	[dist], 
	[lng], 
	[lat], 
	[x], 
	[y]
	)
SELECT [id],  
right('000000000000'+ rtrim(case stop when 'null' then null else stop end), 5) as stop, /*Left pad with 0 to 5 digits*/
[service], 
[direction],
[seq], 
[description], 
[road],
[station] , 
[dist],
[lng], 
[lat], 
[x], 
[y]
FROM [STAGING_BusStops];
GO

insert into F_Weekday 
			([src]
           ,[dst]
           ,[hr]
           ,[min]
           ,[km]
           ,[pax])
SELECT right('000000000000'+ rtrim(case src when 'null' then null else src end), 5) as src /*Left pad with 0 to 5 digits*/
      ,right('000000000000'+ rtrim(case dst when 'null' then null else dst end), 5) as dst
	  ,cast(hr as int) as hr
      ,cast(min as decimal(18,4)) as min
      ,cast(km as decimal(18,4)) as km
	  ,cast(replace(pax, CHAR(13), '') as int) as pax  /*Remove carriage return character*/
FROM [transport].[dbo].[STAGING_12Weekday] 

insert into F_Sunday 
			([src]
           ,[dst]
           ,[hr]
           ,[min]
           ,[km]
           ,[pax])
SELECT right('000000000000'+ rtrim(case src when 'null' then null else src end), 5) as src /*Left pad with 0 to 5 digits*/
      ,right('000000000000'+ rtrim(case dst when 'null' then null else dst end), 5) as dst
	  ,cast(hr as int) as hr
      ,cast(min as decimal(18,4)) as min
      ,cast(km as decimal(18,4)) as km
	  ,cast(replace(pax, CHAR(13), '') as int) as pax  /*Remove carriage return character*/
FROM [transport].[dbo].[STAGING_12Sun]*/