# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jan 23 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainGUI
###########################################################################

class MainGUI ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 613,373 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		self.stbMain = self.CreateStatusBar( 2, wx.STB_SIZEGRIP, wx.ID_ANY )
		self.stbMain.SetStatusWidths([-1, 50])
		self.mnbMain = wx.MenuBar( 0 )
		self.mnuFile = wx.Menu()
		self.mnuOpen = wx.MenuItem( self.mnuFile, wx.ID_ANY, u"Open...", u"Select image to open",  wx.ITEM_NORMAL )
		self.mnuFile.Append( self.mnuOpen )
		self.mnuClose = wx.MenuItem( self.mnuFile, wx.ID_ANY, u"Close", u"Close image", wx.ITEM_NORMAL )
		self.mnuClose.Enable( False )
		self.mnuFile.Append( self.mnuClose )
		
		self.mnuFile.AppendSeparator()
		
		self.mnuExit = wx.MenuItem( self.mnuFile, wx.ID_ANY, u"Exit", u"Exit application", wx.ITEM_NORMAL )
		self.mnuFile.Append( self.mnuExit )
		
		self.mnbMain.Append( self.mnuFile, u"&File" ) 
		
		self.SetMenuBar( self.mnbMain )
		
		sizerFrame = wx.BoxSizer( wx.HORIZONTAL )
		
		self.pnlThumbnail = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.pnlThumbnail.SetScrollRate( 5, 5 )
		self.pnlThumbnail.SetMinSize( wx.Size( 100,-1 ) )
		self.pnlThumbnail.SetMaxSize( wx.Size( 100,-1 ) )

		sizerThumb = wx.BoxSizer( wx.VERTICAL )
		
		sizerThumb.SetMinSize( wx.Size( 100,-1 ) ) 
		
		self.pnlThumbnail.SetSizer( sizerThumb )
		self.pnlThumbnail.Layout()
		sizerThumb.Fit( self.pnlThumbnail )
		
		sizerFrame.Add( self.pnlThumbnail, 1, wx.EXPAND |wx.ALL, 1 )
		
		self.pnlImage = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.pnlImage.SetScrollRate( 5, 5 )
		sizerImage = wx.BoxSizer( wx.VERTICAL )
		
		self.bitmapImage = wx.StaticBitmap(self.pnlImage, wx.ID_ANY, wx.Bitmap()) # wx.StaticBitmap( self.pnlImage, wx.ID_ANY, wx.Bitmap( u"../../../Pictures/IMAG0857.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerImage.Add( self.bitmapImage, 1, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 1 )
		
		
		self.pnlImage.SetSizer( sizerImage )
		self.pnlImage.Layout()
		sizerImage.Fit( self.pnlImage )
		sizerFrame.Add( self.pnlImage, 1, wx.EXPAND |wx.ALL, 1 )
		
		
		self.SetSizer( sizerFrame )
		self.Layout()
		self.tlbMain = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY )

		
		self.tlZoomIn = self.tlbMain.AddTool(wx.ID_ANY, u"+", wx.Bitmap(u"zoom-in-16.png"), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, u"Zoom in", None ) #self.tlbMain.AddLabelTool( wx.ID_ANY, u"+", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.tlZoomOut = self.tlbMain.AddTool(wx.ID_ANY, u"-", wx.Bitmap(u"zoom-out-16.png"), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, u"Zoom out", None ) #self.tlbMain.AddLabelTool( wx.ID_ANY, u"-", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.tlbMain.Realize() 
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.onFileOpen, id = self.mnuOpen.GetId() )
		self.Bind( wx.EVT_MENU, self.OnClose, id = self.mnuClose.GetId() )
		self.Bind( wx.EVT_MENU, self.OnExit, id = self.mnuExit.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnZoomIn, id = self.tlZoomIn.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnZoomOut, id = self.tlZoomOut.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onFileOpen( self, event ):
		event.Skip()
	
	def OnClose( self, event ):
		event.Skip()
	
	def OnExit( self, event ):
		event.Skip()
	
	def bitmapImageOnLeftDown( self, event ):
		event.Skip()
	
	def OnZoomIn( self, event ):
		event.Skip()
	
	def OnZoomOut( self, event ):
		event.Skip()
	

