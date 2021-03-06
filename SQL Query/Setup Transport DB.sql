USE [transport]
GO
/****** Object:  Table [dbo].[D_BusRoute]    Script Date: 6/26/2016 3:00:58 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[D_BusRoute](
	[id] [int] NOT NULL,
	[stop] [varchar](5) NULL,
	[service] [int] NULL,
	[direction] [int] NOT NULL,
	[seq] [int] NULL,
	[dist] [float] NULL,
 CONSTRAINT [PK_D_BusRoute] PRIMARY KEY CLUSTERED 
(
	[id] ASC,
	[direction] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
/****** Object:  Table [dbo].[D_BusStops]    Script Date: 6/26/2016 3:00:58 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[D_BusStops](
	[id] [int] NOT NULL,
	[stop] [varchar](5) NULL,
	[description] [varchar](1000) NULL,
	[road] [varchar](100) NULL,
	[station] [varchar](100) NULL,
	[lng] [decimal](18, 4) NULL,
	[lat] [decimal](18, 4) NULL,
	[x] [decimal](18, 4) NULL,
	[y] [decimal](18, 4) NULL,
 CONSTRAINT [PK_D_BusStops] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
/****** Object:  Table [dbo].[F_Service]    Script Date: 6/26/2016 3:00:58 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[F_Service](
	[src] [varchar](5) NULL,
	[dst] [varchar](5) NULL,
	[hr] [int] NULL,
	[min] [numeric](18, 4) NULL,
	[km] [numeric](18, 4) NULL,
	[pax] [int] NULL,
	[dayofweek] [varchar](50) NULL,
	[id] [int] IDENTITY(1,1) NOT NULL,
 CONSTRAINT [PK_F_Service] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
/****** Object:  Table [dbo].[STAGING_12Sun]    Script Date: 6/26/2016 3:00:58 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[STAGING_12Sun](
	[src] [varchar](50) NULL,
	[dst] [varchar](50) NULL,
	[hr] [varchar](50) NULL,
	[min] [varchar](50) NULL,
	[km] [varchar](50) NULL,
	[pax] [varchar](50) NULL
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
/****** Object:  Table [dbo].[STAGING_12Weekday]    Script Date: 6/26/2016 3:00:58 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[STAGING_12Weekday](
	[src] [varchar](50) NULL,
	[dst] [varchar](50) NULL,
	[hr] [varchar](50) NULL,
	[min] [varchar](50) NULL,
	[km] [varchar](50) NULL,
	[pax] [varchar](50) NULL
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
/****** Object:  Table [dbo].[STAGING_BusStops]    Script Date: 6/26/2016 3:00:58 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[STAGING_BusStops](
	[id] [int] NULL,
	[stop] [varchar](5) NULL,
	[service] [int] NULL,
	[direction] [int] NULL,
	[seq] [int] NULL,
	[description] [varchar](1000) NULL,
	[road] [varchar](100) NULL,
	[station] [varchar](100) NULL,
	[dist] [decimal](18, 4) NULL,
	[lng] [decimal](18, 4) NULL,
	[lat] [decimal](18, 4) NULL,
	[x] [decimal](18, 4) NULL,
	[y] [decimal](18, 4) NULL
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
