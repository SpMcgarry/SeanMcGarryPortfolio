from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuration for the first database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///SpmResumeData.db.sql'
app.config['SQLALCHEMY_BINDS'] = {
    'sigmintdata': 'sqlite:///sigmintdata.db.sql'
}

# Create a single SQLAlchemy instance
db = SQLAlchemy(app)

# Import models from the specialMints/models directory
from specialMints.models import Comic, Collectible

# Define a model for your database table
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

@app.route("/")
def home():
    # Create a sample item and add it to the database
    with app.app_context():
        db.create_all()
        item = Item(name="Sample Item")
        db.session.add(item)
        db.session.commit()
    return """
    
    <html>
        <head>
            <title>Main Page</title>
        </head>
        <body>
            <h1><html xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:w="urn:schemas-microsoft-com:office:word" xmlns:m="http://schemas.microsoft.com/office/2004/12/omml" xmlns="http://www.w3.org/TR/REC-html40"><head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta name="ProgId" content="Word.Document">
<meta name="Generator" content="Microsoft Word 15">
<meta name="Originator" content="Microsoft Word 15">
<link rel="File-List" href="Sean_McGarry_Resume_web.fld/filelist.xml">
<!--[if gte mso 9]><xml>
 <o:DocumentProperties>
  <o:Author>McGarry, Sean</o:Author>
  <o:LastAuthor>McGarry, Sean</o:LastAuthor>
  <o:Revision>3</o:Revision>
  <o:TotalTime>56</o:TotalTime>
  <o:LastPrinted>2024-02-08T16:42:00Z</o:LastPrinted>
  <o:Created>2024-03-02T05:14:00Z</o:Created>
  <o:LastSaved>2024-03-02T05:59:00Z</o:LastSaved>
  <o:Pages>1</o:Pages>
  <o:Words>1277</o:Words>
  <o:Characters>7281</o:Characters>
  <o:Lines>60</o:Lines>
  <o:Paragraphs>17</o:Paragraphs>
  <o:CharactersWithSpaces>8541</o:CharactersWithSpaces>
  <o:Version>16.00</o:Version>
 </o:DocumentProperties>
 <o:OfficeDocumentSettings>
  <o:AllowPNG/>
 </o:OfficeDocumentSettings>
</xml><![endif]-->
<link rel="dataStoreItem" href="Sean_McGarry_Resume_web.fld/item0007.xml" target="Sean_McGarry_Resume_web.fld/props008.xml">
<link rel="themeData" href="Sean_McGarry_Resume_web.fld/themedata.thmx">
<link rel="colorSchemeMapping" href="Sean_McGarry_Resume_web.fld/colorschememapping.xml">
<!--[if gte mso 9]><xml>
 <w:WordDocument>
  <w:SpellingState>Clean</w:SpellingState>
  <w:GrammarState>Clean</w:GrammarState>
  <w:TrackMoves>false</w:TrackMoves>
  <w:TrackFormatting/>
  <w:PunctuationKerning/>
  <w:ValidateAgainstSchemas/>
  <w:SaveIfXMLInvalid>false</w:SaveIfXMLInvalid>
  <w:IgnoreMixedContent>false</w:IgnoreMixedContent>
  <w:AlwaysShowPlaceholderText>false</w:AlwaysShowPlaceholderText>
  <w:DoNotPromoteQF/>
  <w:LidThemeOther>EN-US</w:LidThemeOther>
  <w:LidThemeAsian>X-NONE</w:LidThemeAsian>
  <w:LidThemeComplexScript>X-NONE</w:LidThemeComplexScript>
  <w:Compatibility>
   <w:BreakWrappedTables/>
   <w:SnapToGridInCell/>
   <w:WrapTextWithPunct/>
   <w:UseAsianBreakRules/>
   <w:DontGrowAutofit/>
   <w:SplitPgBreakAndParaMark/>
   <w:EnableOpenTypeKerning/>
   <w:DontFlipMirrorIndents/>
   <w:OverrideTableStyleHps/>
  </w:Compatibility>
  <m:mathPr>
   <m:mathFont m:val="Cambria Math"/>
   <m:brkBin m:val="before"/>
   <m:brkBinSub m:val="&#45;-"/>
   <m:smallFrac m:val="off"/>
   <m:dispDef/>
   <m:lMargin m:val="0"/>
   <m:rMargin m:val="0"/>
   <m:defJc m:val="centerGroup"/>
   <m:wrapIndent m:val="1440"/>
   <m:intLim m:val="subSup"/>
   <m:naryLim m:val="undOvr"/>
  </m:mathPr></w:WordDocument>
</xml><![endif]--><!--[if gte mso 9]><xml>
 <w:LatentStyles DefLockedState="false" DefUnhideWhenUsed="false"
  DefSemiHidden="false" DefQFormat="false" DefPriority="99"
  LatentStyleCount="376">
  <w:LsdException Locked="false" Priority="0" QFormat="true" Name="Normal"/>
  <w:LsdException Locked="false" Priority="9" QFormat="true" Name="heading 1"/>
  <w:LsdException Locked="false" Priority="9" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="heading 2"/>
  <w:LsdException Locked="false" Priority="9" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="heading 3"/>
  <w:LsdException Locked="false" Priority="9" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="heading 4"/>
  <w:LsdException Locked="false" Priority="9" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="heading 5"/>
  <w:LsdException Locked="false" Priority="9" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="heading 6"/>
  <w:LsdException Locked="false" Priority="9" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="heading 7"/>
  <w:LsdException Locked="false" Priority="9" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="heading 8"/>
  <w:LsdException Locked="false" Priority="9" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="heading 9"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="index 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="index 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="index 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="index 4"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="index 5"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="index 6"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="index 7"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="index 8"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="index 9"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" Name="toc 1"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" Name="toc 2"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" Name="toc 3"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" Name="toc 4"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" Name="toc 5"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" Name="toc 6"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" Name="toc 7"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" Name="toc 8"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" Name="toc 9"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Normal Indent"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="footnote text"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="annotation text"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="header"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="footer"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="index heading"/>
  <w:LsdException Locked="false" Priority="35" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="caption"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="table of figures"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="envelope address"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="envelope return"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="footnote reference"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="annotation reference"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="line number"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="page number"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="endnote reference"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="endnote text"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="table of authorities"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="macro"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="toa heading"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Bullet"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Number"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List 4"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List 5"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Bullet 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Bullet 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Bullet 4"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Bullet 5"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Number 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Number 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Number 4"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Number 5"/>
  <w:LsdException Locked="false" Priority="10" QFormat="true" Name="Title"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Closing"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Signature"/>
  <w:LsdException Locked="false" Priority="1" SemiHidden="true"
   UnhideWhenUsed="true" Name="Default Paragraph Font"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Body Text"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Body Text Indent"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Continue"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Continue 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Continue 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Continue 4"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="List Continue 5"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Message Header"/>
  <w:LsdException Locked="false" Priority="11" QFormat="true" Name="Subtitle"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Salutation"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Date"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Body Text First Indent"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Body Text First Indent 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Note Heading"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Body Text 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Body Text 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Body Text Indent 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Body Text Indent 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Block Text"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Hyperlink"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="FollowedHyperlink"/>
  <w:LsdException Locked="false" Priority="22" QFormat="true" Name="Strong"/>
  <w:LsdException Locked="false" Priority="20" QFormat="true" Name="Emphasis"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Document Map"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Plain Text"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="E-mail Signature"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Top of Form"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Bottom of Form"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Normal (Web)"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Acronym"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Address"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Cite"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Code"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Definition"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Keyboard"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Preformatted"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Sample"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Typewriter"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="HTML Variable"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Normal Table"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="annotation subject"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="No List"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Outline List 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Outline List 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Outline List 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Simple 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Simple 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Simple 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Classic 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Classic 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Classic 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Classic 4"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Colorful 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Colorful 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Colorful 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Columns 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Columns 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Columns 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Columns 4"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Columns 5"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Grid 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Grid 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Grid 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Grid 4"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Grid 5"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Grid 6"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Grid 7"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Grid 8"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table List 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table List 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table List 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table List 4"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table List 5"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table List 6"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table List 7"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table List 8"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table 3D effects 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table 3D effects 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table 3D effects 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Contemporary"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Elegant"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Professional"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Subtle 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Subtle 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Web 1"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Web 2"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Web 3"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Balloon Text"/>
  <w:LsdException Locked="false" Priority="39" Name="Table Grid"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Table Theme"/>
  <w:LsdException Locked="false" SemiHidden="true" Name="Placeholder Text"/>
  <w:LsdException Locked="false" Priority="1" QFormat="true" Name="No Spacing"/>
  <w:LsdException Locked="false" Priority="60" Name="Light Shading"/>
  <w:LsdException Locked="false" Priority="61" Name="Light List"/>
  <w:LsdException Locked="false" Priority="62" Name="Light Grid"/>
  <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1"/>
  <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2"/>
  <w:LsdException Locked="false" Priority="65" Name="Medium List 1"/>
  <w:LsdException Locked="false" Priority="66" Name="Medium List 2"/>
  <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1"/>
  <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2"/>
  <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3"/>
  <w:LsdException Locked="false" Priority="70" Name="Dark List"/>
  <w:LsdException Locked="false" Priority="71" Name="Colorful Shading"/>
  <w:LsdException Locked="false" Priority="72" Name="Colorful List"/>
  <w:LsdException Locked="false" Priority="73" Name="Colorful Grid"/>
  <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 1"/>
  <w:LsdException Locked="false" Priority="61" Name="Light List Accent 1"/>
  <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 1"/>
  <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 1"/>
  <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 1"/>
  <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 1"/>
  <w:LsdException Locked="false" SemiHidden="true" Name="Revision"/>
  <w:LsdException Locked="false" Priority="34" QFormat="true"
   Name="List Paragraph"/>
  <w:LsdException Locked="false" Priority="29" QFormat="true" Name="Quote"/>
  <w:LsdException Locked="false" Priority="30" QFormat="true"
   Name="Intense Quote"/>
  <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 1"/>
  <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 1"/>
  <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 1"/>
  <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 1"/>
  <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 1"/>
  <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 1"/>
  <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 1"/>
  <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 1"/>
  <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 2"/>
  <w:LsdException Locked="false" Priority="61" Name="Light List Accent 2"/>
  <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 2"/>
  <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 2"/>
  <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 2"/>
  <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 2"/>
  <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 2"/>
  <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 2"/>
  <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 2"/>
  <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 2"/>
  <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 2"/>
  <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 2"/>
  <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 2"/>
  <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 2"/>
  <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 3"/>
  <w:LsdException Locked="false" Priority="61" Name="Light List Accent 3"/>
  <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 3"/>
  <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 3"/>
  <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 3"/>
  <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 3"/>
  <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 3"/>
  <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 3"/>
  <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 3"/>
  <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 3"/>
  <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 3"/>
  <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 3"/>
  <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 3"/>
  <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 3"/>
  <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 4"/>
  <w:LsdException Locked="false" Priority="61" Name="Light List Accent 4"/>
  <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 4"/>
  <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 4"/>
  <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 4"/>
  <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 4"/>
  <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 4"/>
  <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 4"/>
  <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 4"/>
  <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 4"/>
  <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 4"/>
  <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 4"/>
  <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 4"/>
  <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 4"/>
  <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 5"/>
  <w:LsdException Locked="false" Priority="61" Name="Light List Accent 5"/>
  <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 5"/>
  <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 5"/>
  <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 5"/>
  <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 5"/>
  <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 5"/>
  <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 5"/>
  <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 5"/>
  <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 5"/>
  <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 5"/>
  <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 5"/>
  <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 5"/>
  <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 5"/>
  <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 6"/>
  <w:LsdException Locked="false" Priority="61" Name="Light List Accent 6"/>
  <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 6"/>
  <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 6"/>
  <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 6"/>
  <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 6"/>
  <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 6"/>
  <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 6"/>
  <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 6"/>
  <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 6"/>
  <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 6"/>
  <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 6"/>
  <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 6"/>
  <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 6"/>
  <w:LsdException Locked="false" Priority="19" QFormat="true"
   Name="Subtle Emphasis"/>
  <w:LsdException Locked="false" Priority="21" QFormat="true"
   Name="Intense Emphasis"/>
  <w:LsdException Locked="false" Priority="31" QFormat="true"
   Name="Subtle Reference"/>
  <w:LsdException Locked="false" Priority="32" QFormat="true"
   Name="Intense Reference"/>
  <w:LsdException Locked="false" Priority="33" QFormat="true" Name="Book Title"/>
  <w:LsdException Locked="false" Priority="37" SemiHidden="true"
   UnhideWhenUsed="true" Name="Bibliography"/>
  <w:LsdException Locked="false" Priority="39" SemiHidden="true"
   UnhideWhenUsed="true" QFormat="true" Name="TOC Heading"/>
  <w:LsdException Locked="false" Priority="41" Name="Plain Table 1"/>
  <w:LsdException Locked="false" Priority="42" Name="Plain Table 2"/>
  <w:LsdException Locked="false" Priority="43" Name="Plain Table 3"/>
  <w:LsdException Locked="false" Priority="44" Name="Plain Table 4"/>
  <w:LsdException Locked="false" Priority="45" Name="Plain Table 5"/>
  <w:LsdException Locked="false" Priority="40" Name="Grid Table Light"/>
  <w:LsdException Locked="false" Priority="46" Name="Grid Table 1 Light"/>
  <w:LsdException Locked="false" Priority="47" Name="Grid Table 2"/>
  <w:LsdException Locked="false" Priority="48" Name="Grid Table 3"/>
  <w:LsdException Locked="false" Priority="49" Name="Grid Table 4"/>
  <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark"/>
  <w:LsdException Locked="false" Priority="51" Name="Grid Table 6 Colorful"/>
  <w:LsdException Locked="false" Priority="52" Name="Grid Table 7 Colorful"/>
  <w:LsdException Locked="false" Priority="46"
   Name="Grid Table 1 Light Accent 1"/>
  <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 1"/>
  <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 1"/>
  <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 1"/>
  <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 1"/>
  <w:LsdException Locked="false" Priority="51"
   Name="Grid Table 6 Colorful Accent 1"/>
  <w:LsdException Locked="false" Priority="52"
   Name="Grid Table 7 Colorful Accent 1"/>
  <w:LsdException Locked="false" Priority="46"
   Name="Grid Table 1 Light Accent 2"/>
  <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 2"/>
  <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 2"/>
  <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 2"/>
  <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 2"/>
  <w:LsdException Locked="false" Priority="51"
   Name="Grid Table 6 Colorful Accent 2"/>
  <w:LsdException Locked="false" Priority="52"
   Name="Grid Table 7 Colorful Accent 2"/>
  <w:LsdException Locked="false" Priority="46"
   Name="Grid Table 1 Light Accent 3"/>
  <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 3"/>
  <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 3"/>
  <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 3"/>
  <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 3"/>
  <w:LsdException Locked="false" Priority="51"
   Name="Grid Table 6 Colorful Accent 3"/>
  <w:LsdException Locked="false" Priority="52"
   Name="Grid Table 7 Colorful Accent 3"/>
  <w:LsdException Locked="false" Priority="46"
   Name="Grid Table 1 Light Accent 4"/>
  <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 4"/>
  <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 4"/>
  <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 4"/>
  <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 4"/>
  <w:LsdException Locked="false" Priority="51"
   Name="Grid Table 6 Colorful Accent 4"/>
  <w:LsdException Locked="false" Priority="52"
   Name="Grid Table 7 Colorful Accent 4"/>
  <w:LsdException Locked="false" Priority="46"
   Name="Grid Table 1 Light Accent 5"/>
  <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 5"/>
  <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 5"/>
  <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 5"/>
  <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 5"/>
  <w:LsdException Locked="false" Priority="51"
   Name="Grid Table 6 Colorful Accent 5"/>
  <w:LsdException Locked="false" Priority="52"
   Name="Grid Table 7 Colorful Accent 5"/>
  <w:LsdException Locked="false" Priority="46"
   Name="Grid Table 1 Light Accent 6"/>
  <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 6"/>
  <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 6"/>
  <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 6"/>
  <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 6"/>
  <w:LsdException Locked="false" Priority="51"
   Name="Grid Table 6 Colorful Accent 6"/>
  <w:LsdException Locked="false" Priority="52"
   Name="Grid Table 7 Colorful Accent 6"/>
  <w:LsdException Locked="false" Priority="46" Name="List Table 1 Light"/>
  <w:LsdException Locked="false" Priority="47" Name="List Table 2"/>
  <w:LsdException Locked="false" Priority="48" Name="List Table 3"/>
  <w:LsdException Locked="false" Priority="49" Name="List Table 4"/>
  <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark"/>
  <w:LsdException Locked="false" Priority="51" Name="List Table 6 Colorful"/>
  <w:LsdException Locked="false" Priority="52" Name="List Table 7 Colorful"/>
  <w:LsdException Locked="false" Priority="46"
   Name="List Table 1 Light Accent 1"/>
  <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 1"/>
  <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 1"/>
  <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 1"/>
  <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 1"/>
  <w:LsdException Locked="false" Priority="51"
   Name="List Table 6 Colorful Accent 1"/>
  <w:LsdException Locked="false" Priority="52"
   Name="List Table 7 Colorful Accent 1"/>
  <w:LsdException Locked="false" Priority="46"
   Name="List Table 1 Light Accent 2"/>
  <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 2"/>
  <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 2"/>
  <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 2"/>
  <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 2"/>
  <w:LsdException Locked="false" Priority="51"
   Name="List Table 6 Colorful Accent 2"/>
  <w:LsdException Locked="false" Priority="52"
   Name="List Table 7 Colorful Accent 2"/>
  <w:LsdException Locked="false" Priority="46"
   Name="List Table 1 Light Accent 3"/>
  <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 3"/>
  <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 3"/>
  <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 3"/>
  <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 3"/>
  <w:LsdException Locked="false" Priority="51"
   Name="List Table 6 Colorful Accent 3"/>
  <w:LsdException Locked="false" Priority="52"
   Name="List Table 7 Colorful Accent 3"/>
  <w:LsdException Locked="false" Priority="46"
   Name="List Table 1 Light Accent 4"/>
  <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 4"/>
  <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 4"/>
  <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 4"/>
  <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 4"/>
  <w:LsdException Locked="false" Priority="51"
   Name="List Table 6 Colorful Accent 4"/>
  <w:LsdException Locked="false" Priority="52"
   Name="List Table 7 Colorful Accent 4"/>
  <w:LsdException Locked="false" Priority="46"
   Name="List Table 1 Light Accent 5"/>
  <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 5"/>
  <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 5"/>
  <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 5"/>
  <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 5"/>
  <w:LsdException Locked="false" Priority="51"
   Name="List Table 6 Colorful Accent 5"/>
  <w:LsdException Locked="false" Priority="52"
   Name="List Table 7 Colorful Accent 5"/>
  <w:LsdException Locked="false" Priority="46"
   Name="List Table 1 Light Accent 6"/>
  <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 6"/>
  <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 6"/>
  <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 6"/>
  <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 6"/>
  <w:LsdException Locked="false" Priority="51"
   Name="List Table 6 Colorful Accent 6"/>
  <w:LsdException Locked="false" Priority="52"
   Name="List Table 7 Colorful Accent 6"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Mention"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Smart Hyperlink"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Hashtag"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Unresolved Mention"/>
  <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
   Name="Smart Link"/>
 </w:LatentStyles>
</xml><![endif]-->
<style>
<!--
 /* Font Definitions */
 @font-face
	{font-family:Wingdings;
	panose-1:5 0 0 0 0 0 0 0 0 0;
	mso-font-charset:2;
	mso-generic-font-family:decorative;
	mso-font-pitch:variable;
	mso-font-signature:3 268435456 0 0 -2147483647 0;}
@font-face
	{font-family:"Cambria Math";
	panose-1:2 4 5 3 5 4 6 3 2 4;
	mso-font-charset:0;
	mso-generic-font-family:roman;
	mso-font-pitch:variable;
	mso-font-signature:-536870145 1107305727 0 0 415 0;}
@font-face
	{font-family:"Calibri Light";
	panose-1:2 15 3 2 2 2 4 3 2 4;
	mso-font-charset:0;
	mso-generic-font-family:swiss;
	mso-font-pitch:variable;
	mso-font-signature:-536859905 -1073732485 9 0 511 0;}
@font-face
	{font-family:CenturyGothic;
	panose-1:2 11 6 4 2 2 2 2 2 4;
	mso-font-alt:Cambria;
	mso-font-charset:0;
	mso-generic-font-family:roman;
	mso-font-pitch:auto;
	mso-font-signature:0 0 0 0 0 0;}
@font-face
	{font-family:"Segoe UI";
	panose-1:2 11 5 2 4 2 4 2 2 3;
	mso-font-charset:0;
	mso-generic-font-family:swiss;
	mso-font-pitch:variable;
	mso-font-signature:-469750017 -1073683329 9 0 511 0;}
@font-face
	{font-family:Roboto;
	panose-1:2 0 0 0 0 0 0 0 0 0;
	mso-font-charset:0;
	mso-generic-font-family:auto;
	mso-font-pitch:variable;
	mso-font-signature:-536868097 1342185855 33 0 415 0;}
 /* Style Definitions */
 p.MsoNormal, li.MsoNormal, div.MsoNormal
	{mso-style-unhide:no;
	mso-style-qformat:yes;
	mso-style-parent:"";
	margin-top:0in;
	margin-right:0in;
	margin-bottom:12.0pt;
	margin-left:.5in;
	text-indent:-.25in;
	line-height:115%;
	mso-pagination:widow-orphan;
	background:white;
	font-size:10.0pt;
	font-family:"Arial",sans-serif;
	mso-fareast-font-family:Arial;
	mso-ansi-language:EN;}
h1
	{mso-style-priority:9;
	mso-style-unhide:no;
	mso-style-qformat:yes;
	mso-style-link:"Heading 1 Char";
	mso-style-next:Normal;
	margin-top:6.0pt;
	margin-right:0in;
	margin-bottom:6.0pt;
	margin-left:.5in;
	mso-add-space:auto;
	text-indent:-.25in;
	mso-pagination:widow-orphan lines-together;
	page-break-after:avoid;
	mso-outline-level:1;
	background:white;
	font-size:14.0pt;
	mso-bidi-font-size:20.0pt;
	font-family:"Arial",sans-serif;
	mso-fareast-font-family:Arial;
	mso-font-kerning:0pt;
	mso-ansi-language:EN;
	font-weight:normal;}
h1.CxSpFirst
	{mso-style-priority:9;
	mso-style-unhide:no;
	mso-style-qformat:yes;
	mso-style-link:"Heading 1 Char";
	mso-style-next:Normal;
	mso-style-type:export-only;
	margin-top:6.0pt;
	margin-right:0in;
	margin-bottom:0in;
	margin-left:.5in;
	mso-add-space:auto;
	text-indent:-.25in;
	mso-pagination:widow-orphan lines-together;
	page-break-after:avoid;
	mso-outline-level:1;
	background:white;
	font-size:14.0pt;
	mso-bidi-font-size:20.0pt;
	font-family:"Arial",sans-serif;
	mso-fareast-font-family:Arial;
	mso-font-kerning:0pt;
	mso-ansi-language:EN;
	font-weight:normal;}
h1.CxSpMiddle
	{mso-style-priority:9;
	mso-style-unhide:no;
	mso-style-qformat:yes;
	mso-style-link:"Heading 1 Char";
	mso-style-next:Normal;
	mso-style-type:export-only;
	margin-top:0in;
	margin-right:0in;
	margin-bottom:0in;
	margin-left:.5in;
	mso-add-space:auto;
	text-indent:-.25in;
	mso-pagination:widow-orphan lines-together;
	page-break-after:avoid;
	mso-outline-level:1;
	background:white;
	font-size:14.0pt;
	mso-bidi-font-size:20.0pt;
	font-family:"Arial",sans-serif;
	mso-fareast-font-family:Arial;
	mso-font-kerning:0pt;
	mso-ansi-language:EN;
	font-weight:normal;}
h1.CxSpLast
	{mso-style-priority:9;
	mso-style-unhide:no;
	mso-style-qformat:yes;
	mso-style-link:"Heading 1 Char";
	mso-style-next:Normal;
	mso-style-type:export-only;
	margin-top:0in;
	margin-right:0in;
	margin-bottom:6.0pt;
	margin-left:.5in;
	mso-add-space:auto;
	text-indent:-.25in;
	mso-pagination:widow-orphan lines-together;
	page-break-after:avoid;
	mso-outline-level:1;
	background:white;
	font-size:14.0pt;
	mso-bidi-font-size:20.0pt;
	font-family:"Arial",sans-serif;
	mso-fareast-font-family:Arial;
	mso-font-kerning:0pt;
	mso-ansi-language:EN;
	font-weight:normal;}
h2
	{mso-style-priority:9;
	mso-style-qformat:yes;
	mso-style-link:"Heading 2 Char";
	mso-style-next:Normal;
	margin-top:0in;
	margin-right:0in;
	margin-bottom:6.0pt;
	margin-left:.5in;
	text-indent:-.25in;
	mso-pagination:widow-orphan lines-together;
	page-break-after:avoid;
	mso-outline-level:2;
	background:white;
	font-size:14.0pt;
	mso-bidi-font-size:16.0pt;
	font-family:"Arial",sans-serif;
	mso-fareast-font-family:Arial;
	mso-ansi-language:EN;
	font-weight:normal;}
h3
	{mso-style-priority:9;
	mso-style-qformat:yes;
	mso-style-link:"Heading 3 Char";
	mso-style-next:Normal;
	margin-top:12.0pt;
	margin-right:0in;
	margin-bottom:0in;
	margin-left:.5in;
	text-indent:-.25in;
	mso-pagination:widow-orphan lines-together;
	page-break-after:avoid;
	mso-outline-level:3;
	tab-stops:3.0in right 7.0in;
	background:white;
	font-size:12.0pt;
	mso-bidi-font-size:14.0pt;
	font-family:"Arial",sans-serif;
	mso-fareast-font-family:Arial;
	color:black;
	mso-themecolor:text1;
	mso-ansi-language:EN;
	font-weight:normal;}
h4
	{mso-style-priority:9;
	mso-style-qformat:yes;
	mso-style-link:"Heading 4 Char";
	mso-style-next:Normal;
	margin-top:0in;
	margin-right:0in;
	margin-bottom:0in;
	margin-left:.5in;
	text-indent:-.25in;
	mso-pagination:widow-orphan lines-together;
	page-break-after:avoid;
	mso-outline-level:4;
	background:white;
	font-size:10.0pt;
	mso-bidi-font-size:12.0pt;
	font-family:"Arial",sans-serif;
	mso-fareast-font-family:Arial;
	color:black;
	mso-themecolor:text1;
	mso-ansi-language:EN;
	font-weight:normal;
	font-style:italic;
	mso-bidi-font-style:normal;}
p.MsoHeader, li.MsoHeader, div.MsoHeader
	{mso-style-priority:99;
	mso-style-link:"Header Char";
	margin-top:0in;
	margin-right:0in;
	margin-bottom:0in;
	margin-left:.5in;
	text-indent:-.25in;
	mso-pagination:widow-orphan;
	tab-stops:center 3.25in right 6.5in;
	background:white;
	font-size:10.0pt;
	font-family:"Arial",sans-serif;
	mso-fareast-font-family:Arial;
	mso-ansi-language:EN;}
p.MsoFooter, li.MsoFooter, div.MsoFooter
	{mso-style-priority:99;
	mso-style-link:"Footer Char";
	margin-top:0in;
	margin-right:0in;
	margin-bottom:0in;
	margin-left:.5in;
	text-indent:-.25in;
	mso-pagination:widow-orphan;
	tab-stops:center 3.25in right 6.5in;
	background:white;
	font-size:10.0pt;
	font-family:"Arial",sans-serif;
	mso-fareast-font-family:Arial;
	mso-ansi-language:EN;}
a:link, span.MsoHyperlink
	{mso-style-priority:99;
	color:#0563C1;
	mso-themecolor:hyperlink;
	text-decoration:underline;
	text-underline:single;}
a:visited, span.MsoHyperlinkFollowed
	{mso-style-noshow:yes;
	mso-style-priority:99;
	color:#954F72;
	mso-themecolor:followedhyperlink;
	text-decoration:underline;
	text-underline:single;}
p
	{mso-style-priority:99;
	mso-margin-top-alt:auto;
	margin-right:0in;
	mso-margin-bottom-alt:auto;
	margin-left:0in;
	mso-pagination:widow-orphan;
	font-size:12.0pt;
	font-family:"Times New Roman",serif;
	mso-fareast-font-family:"Times New Roman";}
p.MsoListParagraph, li.MsoListParagraph, div.MsoListParagraph
	{mso-style-priority:34;
	mso-style-unhide:no;
	mso-style-qformat:yes;
	margin-top:0in;
	margin-right:0in;
	margin-bottom:12.0pt;
	margin-left:.5in;
	mso-add-space:auto;
	text-indent:-.25in;
	line-height:115%;
	mso-pagination:widow-orphan;
	background:white;
	font-size:10.0pt;
	font-family:"Arial",sans-serif;
	mso-fareast-font-family:Arial;
	mso-ansi-language:EN;}
p.MsoListParagraphCxSpFirst, li.MsoListParagraphCxSpFirst, div.MsoListParagraphCxSpFirst
	{mso-style-priority:34;
	mso-style-unhide:no;
	mso-style-qformat:yes;
	mso-style-type:export-only;
	margin-top:0in;
	margin-right:0in;
	margin-bottom:0in;
	margin-left:.5in;
	mso-add-space:auto;
	text-indent:-.25in;
	line-height:115%;
	mso-pagination:widow-orphan;
	background:white;
	font-size:10.0pt;
	font-family:"Arial",sans-serif;
	mso-fareast-font-family:Arial;
	mso-ansi-language:EN;}
p.MsoListParagraphCxSpMiddle, li.MsoListParagraphCxSpMiddle, div.MsoListParagraphCxSpMiddle
	{mso-style-priority:34;
	mso-style-unhide:no;
	mso-style-qformat:yes;
	mso-style-type:export-only;
	margin-top:0in;
	margin-right:0in;
	margin-bottom:0in;
	margin-left:.5in;
	mso-add-space:auto;
	text-indent:-.25in;
	line-height:115%;
	mso-pagination:widow-orphan;
	background:white;
	font-size:10.0pt;
	font-family:"Arial",sans-serif;
	mso-fareast-font-family:Arial;
	mso-ansi-language:EN;}
p.MsoListParagraphCxSpLast, li.MsoListParagraphCxSpLast, div.MsoListParagraphCxSpLast
	{mso-style-priority:34;
	mso-style-unhide:no;
	mso-style-qformat:yes;
	mso-style-type:export-only;
	margin-top:0in;
	margin-right:0in;
	margin-bottom:12.0pt;
	margin-left:.5in;
	mso-add-space:auto;
	text-indent:-.25in;
	line-height:115%;
	mso-pagination:widow-orphan;
	background:white;
	font-size:10.0pt;
	font-family:"Arial",sans-serif;
	mso-fareast-font-family:Arial;
	mso-ansi-language:EN;}
span.Heading1Char
	{mso-style-name:"Heading 1 Char";
	mso-style-priority:9;
	mso-style-unhide:no;
	mso-style-locked:yes;
	mso-style-link:"Heading 1";
	mso-ansi-font-size:14.0pt;
	mso-bidi-font-size:20.0pt;
	font-family:"Arial",sans-serif;
	mso-ascii-font-family:Arial;
	mso-fareast-font-family:Arial;
	mso-hansi-font-family:Arial;
	mso-bidi-font-family:Arial;
	background:white;
	mso-ansi-language:EN;}
span.Heading2Char
	{mso-style-name:"Heading 2 Char";
	mso-style-priority:9;
	mso-style-unhide:no;
	mso-style-locked:yes;
	mso-style-link:"Heading 2";
	mso-ansi-font-size:14.0pt;
	mso-bidi-font-size:16.0pt;
	font-family:"Arial",sans-serif;
	mso-ascii-font-family:Arial;
	mso-fareast-font-family:Arial;
	mso-hansi-font-family:Arial;
	mso-bidi-font-family:Arial;
	background:white;
	mso-ansi-language:EN;}
span.Heading3Char
	{mso-style-name:"Heading 3 Char";
	mso-style-priority:9;
	mso-style-unhide:no;
	mso-style-locked:yes;
	mso-style-link:"Heading 3";
	mso-bidi-font-size:14.0pt;
	font-family:"Arial",sans-serif;
	mso-ascii-font-family:Arial;
	mso-fareast-font-family:Arial;
	mso-hansi-font-family:Arial;
	mso-bidi-font-family:Arial;
	color:black;
	mso-themecolor:text1;
	background:white;
	mso-ansi-language:EN;}
span.Heading4Char
	{mso-style-name:"Heading 4 Char";
	mso-style-priority:9;
	mso-style-unhide:no;
	mso-style-locked:yes;
	mso-style-link:"Heading 4";
	mso-ansi-font-size:10.0pt;
	font-family:"Arial",sans-serif;
	mso-ascii-font-family:Arial;
	mso-fareast-font-family:Arial;
	mso-hansi-font-family:Arial;
	mso-bidi-font-family:Arial;
	color:black;
	mso-themecolor:text1;
	background:white;
	mso-ansi-language:EN;
	font-style:italic;
	mso-bidi-font-style:normal;}
span.HeaderChar
	{mso-style-name:"Header Char";
	mso-style-priority:99;
	mso-style-unhide:no;
	mso-style-locked:yes;
	mso-style-link:Header;
	mso-ansi-font-size:10.0pt;
	mso-bidi-font-size:10.0pt;
	font-family:"Arial",sans-serif;
	mso-ascii-font-family:Arial;
	mso-fareast-font-family:Arial;
	mso-hansi-font-family:Arial;
	mso-bidi-font-family:Arial;
	background:white;
	mso-ansi-language:EN;}
span.FooterChar
	{mso-style-name:"Footer Char";
	mso-style-priority:99;
	mso-style-unhide:no;
	mso-style-locked:yes;
	mso-style-link:Footer;
	mso-ansi-font-size:10.0pt;
	mso-bidi-font-size:10.0pt;
	font-family:"Arial",sans-serif;
	mso-ascii-font-family:Arial;
	mso-fareast-font-family:Arial;
	mso-hansi-font-family:Arial;
	mso-bidi-font-family:Arial;
	background:white;
	mso-ansi-language:EN;}
span.SpellE
	{mso-style-name:"";
	mso-spl-e:yes;}
span.GramE
	{mso-style-name:"";
	mso-gram-e:yes;}
.MsoChpDefault
	{mso-style-type:export-only;
	mso-default-props:yes;
	mso-ascii-font-family:Calibri;
	mso-ascii-theme-font:minor-latin;
	mso-fareast-font-family:Calibri;
	mso-fareast-theme-font:minor-latin;
	mso-hansi-font-family:Calibri;
	mso-hansi-theme-font:minor-latin;
	mso-bidi-font-family:"Times New Roman";
	mso-bidi-theme-font:minor-bidi;
	mso-font-kerning:0pt;
	mso-ligatures:none;}
 /* Page Definitions */
 @page
	{mso-footnote-separator:url("Sean_McGarry_Resume_web.fld/header.html") fs;
	mso-footnote-continuation-separator:url("Sean_McGarry_Resume_web.fld/header.html") fcs;
	mso-endnote-separator:url("Sean_McGarry_Resume_web.fld/header.html") es;
	mso-endnote-continuation-separator:url("Sean_McGarry_Resume_web.fld/header.html") ecs;}
@page WordSection1
	{size:8.5in 11.0in;
	margin:.8in .5in .5in .5in;
	mso-header-margin:.5in;
	mso-footer-margin:.5in;
	mso-title-page:yes;
	mso-even-header:url("Sean_McGarry_Resume_web.fld/header.html") eh1;
	mso-header:url("Sean_McGarry_Resume_web.fld/header.html") h1;
	mso-even-footer:url("Sean_McGarry_Resume_web.fld/header.html") ef1;
	mso-footer:url("Sean_McGarry_Resume_web.fld/header.html") f1;
	mso-first-header:url("Sean_McGarry_Resume_web.fld/header.html") fh1;
	mso-first-footer:url("Sean_McGarry_Resume_web.fld/header.html") ff1;
	mso-paper-source:0;}
div.WordSection1
	{page:WordSection1;}
 /* List Definitions */
 @list l0
	{mso-list-id:264268334;
	mso-list-type:hybrid;
	mso-list-template-ids:1472343958 67698689 67698691 67698693 67698689 67698691 67698693 67698689 67698691 67698693;}
@list l0:level1
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	font-family:Symbol;}
@list l0:level2
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	font-family:"Courier New";}
@list l0:level3
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	font-family:Wingdings;}
@list l0:level4
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	font-family:Symbol;}
@list l0:level5
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	font-family:"Courier New";}
@list l0:level6
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	font-family:Wingdings;}
@list l0:level7
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	font-family:Symbol;}
@list l0:level8
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	font-family:"Courier New";}
@list l0:level9
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	font-family:Wingdings;}
@list l1
	{mso-list-id:451632193;
	mso-list-type:hybrid;
	mso-list-template-ids:-237846218 67698689 67698691 67698693 67698689 67698691 67698693 67698689 67698691 67698693;}
@list l1:level1
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:1.0in;
	text-indent:-.25in;
	font-family:Symbol;}
@list l1:level2
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:1.5in;
	text-indent:-.25in;
	font-family:"Courier New";}
@list l1:level3
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:2.0in;
	text-indent:-.25in;
	font-family:Wingdings;}
@list l1:level4
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:2.5in;
	text-indent:-.25in;
	font-family:Symbol;}
@list l1:level5
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:3.0in;
	text-indent:-.25in;
	font-family:"Courier New";}
@list l1:level6
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:3.5in;
	text-indent:-.25in;
	font-family:Wingdings;}
@list l1:level7
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:4.0in;
	text-indent:-.25in;
	font-family:Symbol;}
@list l1:level8
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:4.5in;
	text-indent:-.25in;
	font-family:"Courier New";}
@list l1:level9
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:5.0in;
	text-indent:-.25in;
	font-family:Wingdings;}
@list l2
	{mso-list-id:566569095;
	mso-list-template-ids:232584712;}
@list l2:level1
	{mso-level-number-format:bullet;
	mso-level-text:●;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l2:level2
	{mso-level-number-format:bullet;
	mso-level-text:○;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l2:level3
	{mso-level-number-format:bullet;
	mso-level-text:■;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l2:level4
	{mso-level-number-format:bullet;
	mso-level-text:●;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l2:level5
	{mso-level-number-format:bullet;
	mso-level-text:○;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l2:level6
	{mso-level-number-format:bullet;
	mso-level-text:■;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l2:level7
	{mso-level-number-format:bullet;
	mso-level-text:●;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l2:level8
	{mso-level-number-format:bullet;
	mso-level-text:○;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l2:level9
	{mso-level-number-format:bullet;
	mso-level-text:■;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l3
	{mso-list-id:643630775;
	mso-list-type:hybrid;
	mso-list-template-ids:-1755809338 67698689 67698691 67698693 67698689 67698691 67698693 67698689 67698691 67698693;}
@list l3:level1
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	font-family:Symbol;}
@list l3:level2
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	font-family:"Courier New";}
@list l3:level3
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	font-family:Wingdings;}
@list l3:level4
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	font-family:Symbol;}
@list l3:level5
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	font-family:"Courier New";}
@list l3:level6
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	font-family:Wingdings;}
@list l3:level7
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	font-family:Symbol;}
@list l3:level8
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	font-family:"Courier New";}
@list l3:level9
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	font-family:Wingdings;}
@list l4
	{mso-list-id:652181382;
	mso-list-template-ids:-124363334;}
@list l4:level1
	{mso-level-number-format:bullet;
	mso-level-text:●;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l4:level2
	{mso-level-number-format:bullet;
	mso-level-text:○;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l4:level3
	{mso-level-number-format:bullet;
	mso-level-text:■;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l4:level4
	{mso-level-number-format:bullet;
	mso-level-text:●;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l4:level5
	{mso-level-number-format:bullet;
	mso-level-text:○;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l4:level6
	{mso-level-number-format:bullet;
	mso-level-text:■;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l4:level7
	{mso-level-number-format:bullet;
	mso-level-text:●;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l4:level8
	{mso-level-number-format:bullet;
	mso-level-text:○;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l4:level9
	{mso-level-number-format:bullet;
	mso-level-text:■;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l5
	{mso-list-id:822431395;
	mso-list-template-ids:-127924152;}
@list l5:level1
	{mso-level-number-format:bullet;
	mso-level-text:●;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l5:level2
	{mso-level-number-format:bullet;
	mso-level-text:○;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l5:level3
	{mso-level-number-format:bullet;
	mso-level-text:■;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l5:level4
	{mso-level-number-format:bullet;
	mso-level-text:●;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l5:level5
	{mso-level-number-format:bullet;
	mso-level-text:○;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l5:level6
	{mso-level-number-format:bullet;
	mso-level-text:■;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l5:level7
	{mso-level-number-format:bullet;
	mso-level-text:●;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l5:level8
	{mso-level-number-format:bullet;
	mso-level-text:○;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l5:level9
	{mso-level-number-format:bullet;
	mso-level-text:■;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l6
	{mso-list-id:1072117582;
	mso-list-template-ids:-481905964;}
@list l6:level1
	{mso-level-number-format:bullet;
	mso-level-text:●;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l6:level2
	{mso-level-number-format:bullet;
	mso-level-text:○;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l6:level3
	{mso-level-number-format:bullet;
	mso-level-text:■;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l6:level4
	{mso-level-number-format:bullet;
	mso-level-text:●;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l6:level5
	{mso-level-number-format:bullet;
	mso-level-text:○;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l6:level6
	{mso-level-number-format:bullet;
	mso-level-text:■;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l6:level7
	{mso-level-number-format:bullet;
	mso-level-text:●;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l6:level8
	{mso-level-number-format:bullet;
	mso-level-text:○;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l6:level9
	{mso-level-number-format:bullet;
	mso-level-text:■;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l7
	{mso-list-id:1381783153;
	mso-list-type:hybrid;
	mso-list-template-ids:-474291974 67698689 67698691 67698693 67698689 67698691 67698693 67698689 67698691 67698693;}
@list l7:level1
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	font-family:Symbol;}
@list l7:level2
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	font-family:"Courier New";}
@list l7:level3
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	font-family:Wingdings;}
@list l7:level4
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	font-family:Symbol;}
@list l7:level5
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	font-family:"Courier New";}
@list l7:level6
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	font-family:Wingdings;}
@list l7:level7
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	font-family:Symbol;}
@list l7:level8
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	font-family:"Courier New";}
@list l7:level9
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	font-family:Wingdings;}
@list l8
	{mso-list-id:1519193373;
	mso-list-template-ids:1676458950;}
@list l8:level1
	{mso-level-number-format:bullet;
	mso-level-text:●;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l8:level2
	{mso-level-number-format:bullet;
	mso-level-text:○;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l8:level3
	{mso-level-number-format:bullet;
	mso-level-text:■;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l8:level4
	{mso-level-number-format:bullet;
	mso-level-text:●;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l8:level5
	{mso-level-number-format:bullet;
	mso-level-text:○;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l8:level6
	{mso-level-number-format:bullet;
	mso-level-text:■;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l8:level7
	{mso-level-number-format:bullet;
	mso-level-text:●;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l8:level8
	{mso-level-number-format:bullet;
	mso-level-text:○;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l8:level9
	{mso-level-number-format:bullet;
	mso-level-text:■;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l9
	{mso-list-id:1570656610;
	mso-list-template-ids:-1596298398;}
@list l9:level1
	{mso-level-number-format:bullet;
	mso-level-text:●;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l9:level2
	{mso-level-number-format:bullet;
	mso-level-text:○;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l9:level3
	{mso-level-number-format:bullet;
	mso-level-text:■;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l9:level4
	{mso-level-number-format:bullet;
	mso-level-text:●;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l9:level5
	{mso-level-number-format:bullet;
	mso-level-text:○;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l9:level6
	{mso-level-number-format:bullet;
	mso-level-text:■;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l9:level7
	{mso-level-number-format:bullet;
	mso-level-text:●;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l9:level8
	{mso-level-number-format:bullet;
	mso-level-text:○;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l9:level9
	{mso-level-number-format:bullet;
	mso-level-text:■;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l10
	{mso-list-id:1642660377;
	mso-list-template-ids:1054220860;}
@list l10:level1
	{mso-level-number-format:bullet;
	mso-level-text:●;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l10:level2
	{mso-level-number-format:bullet;
	mso-level-text:○;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l10:level3
	{mso-level-number-format:bullet;
	mso-level-text:■;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l10:level4
	{mso-level-number-format:bullet;
	mso-level-text:●;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l10:level5
	{mso-level-number-format:bullet;
	mso-level-text:○;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l10:level6
	{mso-level-number-format:bullet;
	mso-level-text:■;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l10:level7
	{mso-level-number-format:bullet;
	mso-level-text:●;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l10:level8
	{mso-level-number-format:bullet;
	mso-level-text:○;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l10:level9
	{mso-level-number-format:bullet;
	mso-level-text:■;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	text-decoration:none;
	text-underline:none;}
@list l11
	{mso-list-id:1889491071;
	mso-list-type:hybrid;
	mso-list-template-ids:-1518063744 67698689 67698691 67698693 67698689 67698691 67698693 67698689 67698691 67698693;}
@list l11:level1
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:1.0in;
	text-indent:-.25in;
	font-family:Symbol;}
@list l11:level2
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:1.5in;
	text-indent:-.25in;
	font-family:"Courier New";}
@list l11:level3
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:2.0in;
	text-indent:-.25in;
	font-family:Wingdings;}
@list l11:level4
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:2.5in;
	text-indent:-.25in;
	font-family:Symbol;}
@list l11:level5
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:3.0in;
	text-indent:-.25in;
	font-family:"Courier New";}
@list l11:level6
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:3.5in;
	text-indent:-.25in;
	font-family:Wingdings;}
@list l11:level7
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:4.0in;
	text-indent:-.25in;
	font-family:Symbol;}
@list l11:level8
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:4.5in;
	text-indent:-.25in;
	font-family:"Courier New";}
@list l11:level9
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:5.0in;
	text-indent:-.25in;
	font-family:Wingdings;}
@list l12
	{mso-list-id:1986010624;
	mso-list-type:hybrid;
	mso-list-template-ids:1268910952 -362657270 67698691 67698693 67698689 67698691 67698693 67698689 67698691 67698693;}
@list l12:level1
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	mso-ansi-font-size:10.0pt;
	mso-bidi-font-size:10.0pt;
	font-family:Symbol;}
@list l12:level2
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	font-family:"Courier New";}
@list l12:level3
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	font-family:Wingdings;}
@list l12:level4
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	font-family:Symbol;}
@list l12:level5
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	font-family:"Courier New";}
@list l12:level6
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	font-family:Wingdings;}
@list l12:level7
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	font-family:Symbol;}
@list l12:level8
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	font-family:"Courier New";}
@list l12:level9
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	text-indent:-.25in;
	font-family:Wingdings;}
@list l13
	{mso-list-id:2099667292;
	mso-list-type:hybrid;
	mso-list-template-ids:-2134459112 67698689 67698691 67698693 67698689 67698691 67698693 67698689 67698691 67698693;}
@list l13:level1
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:39.0pt;
	text-indent:-.25in;
	font-family:Symbol;}
@list l13:level2
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:75.0pt;
	text-indent:-.25in;
	font-family:"Courier New";}
@list l13:level3
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:111.0pt;
	text-indent:-.25in;
	font-family:Wingdings;}
@list l13:level4
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:147.0pt;
	text-indent:-.25in;
	font-family:Symbol;}
@list l13:level5
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:183.0pt;
	text-indent:-.25in;
	font-family:"Courier New";}
@list l13:level6
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:219.0pt;
	text-indent:-.25in;
	font-family:Wingdings;}
@list l13:level7
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:255.0pt;
	text-indent:-.25in;
	font-family:Symbol;}
@list l13:level8
	{mso-level-number-format:bullet;
	mso-level-text:o;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:291.0pt;
	text-indent:-.25in;
	font-family:"Courier New";}
@list l13:level9
	{mso-level-number-format:bullet;
	mso-level-text:;
	mso-level-tab-stop:none;
	mso-level-number-position:left;
	margin-left:327.0pt;
	text-indent:-.25in;
	font-family:Wingdings;}
ol
	{margin-bottom:0in;}
ul
	{margin-bottom:0in;}
-->
</style>
<!--[if gte mso 10]>
<style>
 /* Style Definitions */
 table.MsoNormalTable
	{mso-style-name:"Table Normal";
	mso-tstyle-rowband-size:0;
	mso-tstyle-colband-size:0;
	mso-style-noshow:yes;
	mso-style-priority:99;
	mso-style-parent:"";
	mso-padding-alt:0in 5.4pt 0in 5.4pt;
	mso-para-margin:0in;
	mso-pagination:widow-orphan;
	font-size:12.0pt;
	font-family:"Calibri",sans-serif;
	mso-ascii-font-family:Calibri;
	mso-ascii-theme-font:minor-latin;
	mso-hansi-font-family:Calibri;
	mso-hansi-theme-font:minor-latin;
	mso-bidi-font-family:"Times New Roman";
	mso-bidi-theme-font:minor-bidi;}
</style>
<![endif]--><!--[if gte mso 9]><xml>
 <o:shapedefaults v:ext="edit" spidmax="1026"/>
</xml><![endif]--><!--[if gte mso 9]><xml>
 <o:shapelayout v:ext="edit">
  <o:idmap v:ext="edit" data="1"/>
 </o:shapelayout></xml><![endif]-->
</head>

<body lang="EN-US" link="#0563C1" vlink="#954F72" style="tab-interval:.5in;
word-wrap:break-word">

<div class="WordSection1">

<p align="center" style="text-align:center;background:white"><b><span style="font-size:14.0pt;font-family:&quot;CenturyGothic&quot;,serif;color:black;
mso-color-alt:windowtext">Sean P. McGarry</span></b><o:p></o:p></p>

<p align="center" style="text-align:center;background:white"><span style="font-size:10.0pt;font-family:&quot;CenturyGothic&quot;,serif;color:blue">seanmcgarryp@gmail.com</span><o:p></o:p></p>

<p align="center" style="text-align:center;background:white"><b><span style="font-size:10.0pt;font-family:&quot;CenturyGothic&quot;,serif;color:black;
mso-color-alt:windowtext">Westford, MA 01886</span></b><o:p></o:p></p>

<p align="center" style="text-align:center;background:white"><span style="font-size:10.0pt;font-family:&quot;CenturyGothic&quot;,serif;color:black;
mso-color-alt:windowtext">LinkedIn:</span><span style="color:black;mso-color-alt:
windowtext"> </span><span style="font-size:10.5pt;font-family:&quot;Segoe UI&quot;,sans-serif;
color:black;mso-color-alt:windowtext;background:white">www.linkedin.com/in/seanmcgarrytechnologist</span><span style="font-size:10.0pt;font-family:&quot;CenturyGothic&quot;,serif;color:#0230FF"><o:p></o:p></span></p>

<p class="MsoNormal" style="margin:0in;text-align:justify;text-indent:0in"><span lang="EN"><o:p>&nbsp;</o:p></span></p>

<p class="MsoNormal" style="margin-top:12.0pt"><b style="mso-bidi-font-weight:
normal"><span lang="EN" style="font-size:14.0pt;line-height:115%;color:black;
mso-color-alt:windowtext">Summary<a name="_hyzh56rpq378"></a></span></b><b style="mso-bidi-font-weight:normal"><span lang="EN" style="font-size:14.0pt;
line-height:115%"><o:p></o:p></span></b></p>

<div style="mso-element:para-border-div;border:none #D9D9E3 1.0pt;mso-border-alt:
none #D9D9E3 0in;padding:0in 0in 0in 0in;background:white;margin-left:.25in;
margin-right:0in">

<h3 style="margin-top:15.0pt;margin-right:0in;margin-bottom:15.0pt;margin-left:
0in;text-align:justify;text-indent:0in;mso-pagination:widow-orphan;page-break-after:
auto;background:white;border:none;mso-border-alt:none #D9D9E3 0in;padding:0in;
mso-padding-alt:0in 0in 0in 0in"><i style="mso-bidi-font-style:normal"><span lang="EN" style="font-size:11.0pt;mso-fareast-font-family:Roboto;color:#374151">Highly
motivated, technology sales professional with 15+ years of experience. Having contributed
to record sales growth with startups and industry giants such as Apple, <span class="SpellE">Wyebot</span>, and Honeywell. Recently completed an associate
degree in computer science with a focus on software development. A broad
history in business-to-business, hardware, software, SaaS, distribution,
retail, customer service and experience. Passionate about creativity, Individual,
team, business, and account growth. A tenacious drive to discover new markets,
develop customer stories, and find solutions using the greatest technology
while giving excellent experiences, and creating lifelong relationships. <o:p></o:p></span></i></h3>

</div>

<p class="MsoNormal" style="margin-top:12.0pt"><b style="mso-bidi-font-weight:
normal"><span lang="EN" style="color:black;mso-color-alt:windowtext">Relevant Accomplishments:</span><span lang="EN"><o:p></o:p></span></b></p>

<p class="MsoNormal" style="margin-top:0in;margin-right:0in;margin-bottom:0in;
margin-left:.25in;text-align:justify;text-indent:0in"><b><span lang="EN" style="color:#374151">Extensive experience maintaining diagnosing and
troubleshooting demo units </span></b><span lang="EN" style="color:#374151">(Apple
hardware and compatible printers and IOT devices as well as Microsoft and
Chrome devices) Apple shop upkeep, technology installations software updates,
and hardware interpolation. </span></p>

<p class="MsoNormal" style="margin-top:0in;margin-right:0in;margin-bottom:0in;
margin-left:.25in;text-align:justify;text-indent:0in"><b><span lang="EN" style="color:#374151">Exceeding</span><span lang="EN" style="color:black;
mso-color-alt:windowtext"> quarterly sales revenue quotas by 120%-140%</span></b><span lang="EN" style="color:black;mso-color-alt:windowtext"> <i>Contributing to 400%
YOY revenue quarters in multiple teams by using consistent follow-up and
outreach and organizational best practices.</i></span><i><span lang="EN"><o:p></o:p></span></i></p>

<p class="MsoNormal" style="margin-bottom:0in;text-align:justify"><span lang="EN"><o:p>&nbsp;</o:p></span></p>

<p class="MsoNormal" style="margin-top:0in;margin-right:0in;margin-bottom:0in;
margin-left:.25in;text-align:justify;text-indent:0in"><b><span lang="EN" style="color:#374151">Establishing</span><span lang="EN" style="color:black;
mso-color-alt:windowtext"> a multifaceted deal within the K-12 education tech
market</span></b><i><span lang="EN" style="color:black;mso-color-alt:windowtext">
growing an infant territory pipeline from $5k to $100k+ adding almost every
district in the territory in less than 6 months.</span></i></p>

<p class="MsoNormal" style="margin-bottom:0in;text-align:justify"><span lang="EN"><o:p>&nbsp;</o:p></span></p>

<p class="MsoNormal" style="margin-top:0in;margin-right:0in;margin-bottom:0in;
margin-left:.25in;text-align:justify;text-indent:0in"><b><span lang="EN" style="color:#374151">Revitalizing</span><span lang="EN" style="color:black;
mso-color-alt:windowtext"> inside sales efforts under the VP of Sales for the
Americas.</span></b><span lang="EN" style="color:black;mso-color-alt:windowtext">
</span><i style="mso-bidi-font-style:normal"><span lang="EN" style="mso-fareast-font-family:
Roboto;color:#374151">Established and ran inside sales efforts</span><b style="mso-bidi-font-weight:normal"><span lang="EN" style="color:black;
mso-color-alt:windowtext">, </span></b><span lang="EN" style="color:black;
mso-color-alt:windowtext">reorganized for reworking, cleaning Salesforce data,
and implementing strategies for better customer outreach. Recognized for saving
an $80k deal with my outreach strategy.</span><span lang="EN"><o:p></o:p></span></i></p>

<p class="MsoNormal" style="margin-bottom:0in;text-align:justify"><b style="mso-bidi-font-weight:normal"><span lang="EN" style="mso-bidi-font-style:
italic"><o:p>&nbsp;</o:p></span></b></p>

<p class="MsoNormal" style="margin-top:0in;margin-right:0in;margin-bottom:0in;
margin-left:.25in;text-align:justify;text-indent:0in"><b><span lang="EN" style="color:#374151">Recognized</span><span lang="EN" style="color:black;
mso-color-alt:windowtext"> for closing large-scale projects contributing to
exceeding team quota at ADI. </span></b><i><span lang="EN" style="color:#374151">2018</span><span lang="EN" style="color:black;mso-color-alt:windowtext"> attained 115% of quota,
2017 = 109% ,2016 = 105%, trusted “IP champion” and key-holder.</span><span lang="EN"><o:p></o:p></span></i></p>

<p class="MsoNormal" style="margin-bottom:0in;text-align:justify"><i><span lang="EN"><o:p>&nbsp;</o:p></span></i></p>

<p class="MsoNormal" style="margin-top:0in;margin-right:0in;margin-bottom:0in;
margin-left:.25in;text-align:justify;text-indent:0in"><b><span lang="EN" style="color:#374151">Establishing</span><span lang="EN" style="color:black;
mso-color-alt:windowtext"> solid customer service habits and focus on
experiences at Circles</span></b><span lang="EN" style="color:black;mso-color-alt:
windowtext">, <i>promoted to the events/ticket team within the first three
months.</i></span></p>

<p class="MsoNormal" style="margin-bottom:0in;text-align:justify"><span lang="EN"><o:p>&nbsp;</o:p></span></p>

<p class="MsoNormal" style="margin-top:0in;margin-right:0in;margin-bottom:0in;
margin-left:.25in;text-align:justify;text-indent:0in"><b><span lang="EN" style="color:#374151">Acquired</span><span lang="EN" style="color:black;
mso-color-alt:windowtext"> learning skills to quickly adapt to new technology
and software</span></b><span lang="EN" style="color:black;mso-color-alt:windowtext">
<i>recognized for effectively translating these concepts to all types of
customers and clients at Apple. </i></span></p>

<p class="MsoNormal" style="margin-bottom:0in;text-align:justify"><span lang="EN"><o:p>&nbsp;</o:p></span></p>

<p class="MsoNormal" style="margin-top:0in;margin-right:0in;margin-bottom:0in;
margin-left:.25in;text-align:justify;text-indent:0in"><b><span lang="EN" style="color:#374151">Recognized for growing relationships with </span><span lang="EN" style="color:black;mso-color-alt:windowtext">partners. </span></b><i><span lang="EN" style="color:black;mso-color-alt:windowtext">Influenced, trained, and
managed a virtual sales team by focusing on motivation and building mutually
beneficial business plans.</span></i></p>

<p class="MsoNormal" style="margin-bottom:0in;text-align:justify"><span lang="EN"><o:p>&nbsp;</o:p></span></p>

<p class="MsoNormal" style="margin-top:0in;margin-right:0in;margin-bottom:0in;
margin-left:.25in;text-align:justify;text-indent:0in"><b><span lang="EN" style="color:#374151">Successfully</span><span lang="EN" style="color:black;
mso-color-alt:windowtext"> managed and won back key accounts at CompUSA.</span></b><span lang="EN" style="color:black;mso-color-alt:windowtext"> <i>Awarded Employee of
the Month for record purchase order of 100k generated from building a
relationship in the education market.</i></span></p>

<p class="MsoNormal" style="margin-top:0in;margin-right:0in;margin-bottom:0in;
margin-left:13.5pt;text-align:justify;text-indent:-13.5pt"><span lang="EN"><o:p>&nbsp;</o:p></span></p>

<p class="MsoNormal" style="margin:0in;text-align:justify;text-indent:0in"><span lang="EN"><o:p>&nbsp;</o:p></span></p>

<h1 style="margin-left:13.5pt;mso-add-space:auto;text-align:justify;text-indent:
-13.5pt"><span lang="EN" style="color:black;mso-color-alt:windowtext">Education:</span></h1>

<h3 style="margin-left:13.5pt;text-align:justify;text-indent:-13.5pt"><span lang="EN">2020 – 2022<span style="mso-tab-count:1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>Southern
New Hampshire University<span style="mso-tab-count:1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>Nashua,
NH</span></h3>

<h4 style="margin-left:13.5pt;text-align:justify;text-indent:-13.5pt"><span class="GramE"><span lang="EN">Associate</span></span><span lang="EN"> degree in
computer science / software development </span></h4>

<p class="MsoNormal" style="margin:0in;text-align:justify;text-indent:0in"><span lang="EN" style="color:black;mso-color-alt:windowtext">coursework: Introduction
to scripting, programming languages, data structures and algorithms, system analysis
and design, operating platforms, applied statistics for STEM, foundation in application
development.</span></p>

<h3 style="margin-left:13.5pt;text-align:justify;text-indent:-13.5pt"><span lang="EN">2002 – 2004<span style="mso-tab-count:1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>Savannah
College of Art and Design<span style="mso-tab-count:1">&nbsp;&nbsp;&nbsp;&nbsp; </span>Savannah, GA</span></h3>

<h4 style="margin-left:13.5pt;text-indent:-13.5pt"><span lang="EN">Focus on sequential
art and 3D design.</span></h4>

<p class="MsoNormal" style="margin-left:0in;text-indent:0in"><span lang="EN" style="color:black;mso-color-alt:windowtext">Coursework: public speaking, written
communication, 3d design, sequential art, art history, drawing, color theory, graphic
design.</span></p>

<h2 style="margin-left:13.5pt;text-align:justify;text-indent:-13.5pt"><span lang="EN" style="color:black;mso-color-alt:windowtext">Experience:</span></h2>

<h3 style="margin-left:13.5pt;text-align:justify;text-indent:-13.5pt"><span lang="EN" style="mso-bidi-font-size:12.0pt">March 2020 – February 2024<span style="mso-tab-count:1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>Sabbatical<span style="mso-tab-count:1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span> Westford,
Massachusetts<o:p></o:p></span></h3>

<p class="MsoNormal" style="margin-top:0in;margin-right:0in;margin-bottom:0in;
margin-left:9.0pt;text-align:justify;text-indent:-9.0pt"><i><span lang="EN" style="color:black;mso-color-alt:windowtext">Homemaker, Freelance services, Jr
Software Development self-studies, Online Marketplace Seller, student, DIY <span class="GramE">Projects</span> and Home management.</span><span lang="EN"><o:p></o:p></span></i></p>

<p class="MsoListParagraphCxSpFirst" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Through self-directed learning continued software development
education, developing freelancing services offerings while gaining skills in
scripting, business services, data, manual testing, sales, and support. </span><span lang="EN"><o:p></o:p></span></p>

<p class="MsoListParagraphCxSpMiddle" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Created python automation to recognize text on trading cards and to
auto fill SEO items and marketplace listings forms using “<span class="SpellE">Chatgpt</span><span class="GramE">” ,</span> python and text recognition libraries </span></p>

<p class="MsoListParagraphCxSpMiddle" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Developed best practices in SEO Market research, cost / pricing analysis
and product listings. Contributing to 2k in profit with a 5-star customer
rating with an online marketplace over a period of 18 months. </span><span lang="EN"><o:p></o:p></span></p>

<p class="MsoListParagraphCxSpMiddle" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Executed a diverse range project that required extensive planning,
learning, budgeting, and sourcing of materials. Including: electronics repair,
children’s bedroom renovations, painting, carpentry, laminate floor
installation,</span></p>

<p class="MsoListParagraphCxSpMiddle" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">project design, building chicken coop, landscape construction of
play areas, garden structures and appliance repair. I also developed some
fantastic wood fired pizza recipes. </span></p>

<p class="MsoListParagraphCxSpMiddle" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Joined the Massachusetts UI ‘RED” training, program. On registration
list 2020- 2021 limiting re-employment timeline.</span></p>

<p class="MsoListParagraphCxSpLast" style="margin-bottom:0in;mso-add-space:auto;
text-align:justify;text-indent:0in"><span lang="EN"><o:p>&nbsp;</o:p></span></p>

<p class="MsoNormal" style="margin:0in;text-align:justify;text-indent:0in"><span lang="EN" style="font-size:12.0pt;line-height:115%;color:black;mso-color-alt:
windowtext">In response to pandemic induced layoffs, Internal and external
family health concerns </span><span lang="EN" style="font-size:12.0pt;line-height:
115%"><o:p></o:p></span></p>

<p class="MsoListParagraphCxSpFirst" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l12 level1 lfo14"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">I Focused on finding new opportunities and commitments to managing
family care and personal development. </span></p>

<p class="MsoListParagraphCxSpMiddle" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Developed multi-faceted time management and organizational skills
to succeed with supporting a spouse in healthcare, a newborn daughter, </span></p>

<p class="MsoListParagraphCxSpMiddle" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">supporting and optimizing remote learning experience for my son. </span></p>

<p class="MsoListParagraphCxSpLast" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Managed and Implement Household budgets and projects. </span></p>

<h3 style="margin-left:13.5pt;text-align:justify;text-indent:-13.5pt"><span lang="EN">July 2019 – March 2020 <span style="mso-tab-count:1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="SpellE">Wyebot</span><span style="mso-tab-count:1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>Marlborough,
Massachusetts</span></h3>

<h4 style="margin-left:13.5pt;text-align:justify;text-indent:-13.5pt"><span lang="EN">Inside Sales Executive</span></h4>

<p class="MsoNormal" style="margin-top:0in;margin-right:0in;margin-bottom:0in;
margin-left:13.5pt;text-align:justify;text-indent:-13.5pt;line-height:normal"><span lang="EN" style="color:black;mso-color-alt:windowtext">A.I., Wi-Fi analytics SaaS
and hardware start-up<b style="mso-bidi-font-weight:normal">. </b>Reported to
the Sales Manager and VP of Sales</span></p>

<p class="MsoListParagraphCxSpFirst" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Promoted A.I. and Wi-Fi analytics SaaS and hardware solutions in
the education tech sector.</span></p>

<p class="MsoListParagraphCxSpLast" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;line-height:normal;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Collaborating with customer engineering team, gathered user
requirements aligned solutions and assisted in the implementation and post
installation issue analysis and support.</span></p>

<h3 style="margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:9.0pt;
margin-bottom:.0001pt;text-align:justify;text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-size:10.0pt;font-family:Symbol;mso-fareast-font-family:
Symbol;mso-bidi-font-family:Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp; </span></span></span><!--[endif]--><span lang="EN" style="font-size:10.0pt">Contributed to the development of sales
processes, including prospecting, territory growth strategies, cadences, and
CRM structure improvements.<o:p></o:p></span></h3>

<p class="MsoListParagraph" style="margin-left:9.0pt;mso-add-space:auto;
text-align:justify;text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Attained 120% quota leading to development of a territory pipeline
from 5k to 100k+ within 2 quarters in the education IT market.</span></p>

<h3 style="margin-left:13.5pt;text-align:justify;text-indent:-13.5pt"><span lang="EN">September 2018 – March 2019 <span style="mso-tab-count:1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span><span class="SpellE">Oncam</span><span style="mso-tab-count:1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>Billerica
Ma</span></h3>

<h4 style="margin-left:13.5pt;text-align:justify;text-indent:-13.5pt"><span lang="EN">Inside Sales </span></h4>

<p class="MsoNormal" style="margin-top:0in;margin-right:0in;margin-bottom:0in;
margin-left:13.5pt;text-align:justify;text-indent:-13.5pt"><span lang="EN" style="color:black;mso-color-alt:windowtext">UK-based Video Surveillance
Manufacturer. </span></p>

<p class="MsoListParagraphCxSpFirst" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Established standard operating procedures measured goals and drove
the inside sales efforts under the VP of Sales for the Americas.</span></p>

<p class="MsoListParagraphCxSpMiddle" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Planned and developed sales support for the regional sales
directors, channel partners, and engineering team.</span></p>

<p class="MsoListParagraphCxSpMiddle" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Led inside sales efforts, applying problem-solving skills and
logical thinking to restructure the inside sales use of Salesforce CRM,
contributing to positive sales growth for the team."</span></p>

<p class="MsoListParagraphCxSpLast" style="margin-left:9.0pt;mso-add-space:auto;
text-align:justify;text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Contributed to cross-functional collaboration within an
international organization.</span></p>

<h3 style="margin-left:13.5pt;text-align:justify;text-indent:-13.5pt"><span lang="EN" style="mso-bidi-font-size:12.0pt">February 2015 – September 2018<span style="mso-tab-count:1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>ADI Global/ Honeywell<span style="mso-tab-count:1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>Woburn, Massachusetts<o:p></o:p></span></h3>

<h4 style="margin-left:13.5pt;text-align:justify;text-indent:-13.5pt"><span lang="EN">Inside Sales Senior</span></h4>

<p class="MsoListParagraphCxSpFirst" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Managed key accounts, oversaw high volumes of inbound calls, and
developed technological organization and time management best practices that
contributed to team progress."</span></p>

<p class="MsoListParagraphCxSpMiddle" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Managed project quotes, bid submittals, and special pricing
requests for Video Surveillance, Fire, Intrusion, Access Control, and A/V
hardware.</span></p>

<p class="MsoListParagraphCxSpLast" style="margin-left:9.0pt;mso-add-space:auto;
text-align:justify;text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Demonstrated a strong understanding of technical products and
solutions.</span></p>

<h3 style="margin-left:13.5pt;text-align:justify;text-indent:-13.5pt"><span lang="EN" style="color:black;mso-color-alt:windowtext">September 2008 – August
2014<span style="mso-tab-count:1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>Apple Inc.<span style="mso-tab-count:1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span> Cambridge,
Massachusetts</span><span lang="EN" style="color:windowtext;mso-color-alt:windowtext"><o:p></o:p></span></h3>

<h4 style="margin-left:13.5pt;text-align:justify;text-indent:-13.5pt"><span lang="EN">Apple Solutions Consultant | </span></h4>

<p class="MsoListParagraphCxSpFirst" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Managed the customer experience, sales, training, merchandising,
and partnership operations in Apple shops within a shop model.</span></p>

<p class="MsoListParagraphCxSpMiddle" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Built a loyal customer community within the partner retail
environment. Via social and customer services, event promotion best practices </span></p>

<p class="MsoListParagraphCxSpLast" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Developed expertise in Apple products, applications, and services.</span></p>

<h3 style="margin-left:13.5pt;text-align:justify;text-indent:-13.5pt"><span lang="EN">Dec 2007 – September 2008<span style="mso-tab-count:1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>Circles<span style="mso-tab-count:1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>Chelmsford,
Ma.</span></h3>

<h4 style="margin-left:13.5pt;text-align:justify;text-indent:-13.5pt"><span lang="EN">Customer Service Concierge and Ticket Team Representative | |</span></h4>

<p class="MsoListParagraphCxSpFirst" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Worked in high volume phone support for American Express’s phone
Concierge program.</span></p>

<p class="MsoListParagraphCxSpMiddle" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Providing excellent customer service, displayed multitasking
abilities, and made calculated decisions on the fly.</span></p>

<p class="MsoListParagraphCxSpMiddle" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Promoted to "Ticket Specialist," focusing on exemplary
experiences and event reservations.</span></p>

<p class="MsoListParagraphCxSpLast" style="margin-left:9.0pt;mso-add-space:auto;
text-align:justify;text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Exemplified communication Multitasking and problem-solving skills.</span></p>

<h3 style="margin-left:13.5pt;text-align:justify;text-indent:-13.5pt"><span lang="EN" style="color:#535353">2004 – 2008<span style="mso-tab-count:1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span><span lang="EN">CompUSA<span style="mso-tab-count:1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span>Nashua,
NH</span><span lang="EN" style="color:#535353"><o:p></o:p></span></h3>

<h4 style="margin-left:13.5pt;text-align:justify;text-indent:-13.5pt"><span lang="EN">Account Manager, Business Services</span></h4>

<p class="MsoListParagraphCxSpFirst" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Assisted customers in establishing hardware and software
requirements and aligning solutions. </span></p>

<p class="MsoListParagraphCxSpMiddle" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Through active account and technical support, acquired new and
revitalized lost accounts.</span></p>

<p class="MsoListParagraphCxSpMiddle" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Generated a record purchase order of $100k through
relationship-building efforts.</span></p>

<p class="MsoListParagraphCxSpLast" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Developed a good understanding of PC hardware and software systems
and applications.</span></p>

<p class="MsoNormal" style="margin-top:0in;margin-right:0in;margin-bottom:0in;
margin-left:13.5pt;text-align:justify;text-indent:0in"><span lang="EN"><o:p>&nbsp;</o:p></span></p>

<h2 style="margin-left:13.5pt;text-align:justify;text-indent:-13.5pt"><b><span lang="EN" style="font-size:11.0pt;mso-bidi-font-size:12.0pt;color:black;
mso-color-alt:windowtext">Development:</span></b><b><span lang="EN" style="font-size:11.0pt;mso-bidi-font-size:12.0pt"><o:p></o:p></span></b></h2>

<p class="MsoListParagraphCxSpFirst" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Basic programming practices</span></p>

<p class="MsoListParagraphCxSpMiddle" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Object-oriented programming (OOP)</span></p>

<p class="MsoListParagraphCxSpMiddle" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Agile team concepts</span></p>

<p class="MsoListParagraphCxSpMiddle" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">AI prompts</span></p>

<p class="MsoListParagraphCxSpMiddle" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Data Structures </span></p>

<p class="MsoListParagraphCxSpMiddle" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Python</span></p>

<p class="MsoListParagraphCxSpMiddle" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Entry-level software development</span></p>

<p class="MsoListParagraphCxSpMiddle" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Web scraping</span></p>

<p class="MsoListParagraphCxSpMiddle" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Swift</span></p>

<p class="MsoListParagraphCxSpMiddle" style="margin-left:9.0pt;mso-add-space:
auto;text-align:justify;text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Apple Script</span></p>

<p class="MsoListParagraphCxSpLast" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:13.5pt;mso-add-space:auto;text-align:justify;
text-indent:-13.5pt"><span lang="EN"><o:p>&nbsp;</o:p></span></p>

<h2 style="margin-left:13.5pt;text-align:justify;text-indent:-13.5pt"><b><span lang="EN" style="font-size:12.0pt;mso-bidi-font-size:14.0pt;color:black;
mso-color-alt:windowtext">Applications</span></b><b><span lang="EN" style="font-size:12.0pt;mso-bidi-font-size:14.0pt"><o:p></o:p></span></b></h2>

<p class="MsoListParagraphCxSpFirst" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Google Docs </span></p>

<p class="MsoListParagraphCxSpMiddle" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Salesforce</span></p>

<p class="MsoListParagraphCxSpMiddle" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">MS Office</span></p>

<p class="MsoListParagraphCxSpMiddle" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">CRM</span></p>

<p class="MsoListParagraphCxSpMiddle" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Zoom</span></p>

<p class="MsoListParagraphCxSpMiddle" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Apple/Mac OS/iOS </span></p>

<p class="MsoListParagraphCxSpMiddle" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">LinkedIn Navigator </span></p>

<p class="MsoListParagraphCxSpMiddle" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Windows</span></p>

<p class="MsoListParagraphCxSpMiddle" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">VMWare</span></p>

<p class="MsoListParagraphCxSpMiddle" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Cloud computing</span></p>

<p class="MsoListParagraphCxSpMiddle" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Microsoft Teams</span></p>

<p class="MsoListParagraphCxSpMiddle" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Google Meet</span></p>

<p class="MsoListParagraphCxSpMiddle" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Pipedrive </span></p>

<p class="MsoListParagraphCxSpMiddle" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">Visual Studio</span></p>

<p class="MsoListParagraphCxSpMiddle" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">PyCharm</span></p>

<p class="MsoListParagraphCxSpMiddle" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span class="SpellE"><span lang="EN" style="color:black;mso-color-alt:windowtext">Sqlite</span></span></p>

<p class="MsoListParagraphCxSpLast" style="margin-top:0in;margin-right:0in;
margin-bottom:0in;margin-left:9.0pt;mso-add-space:auto;text-align:justify;
text-indent:-9.0pt;mso-list:l7 level1 lfo13"><!--[if !supportLists]--><span lang="EN" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;
</span></span></span><!--[endif]--><span lang="EN" style="color:black;mso-color-alt:
windowtext">XCode</span></p>

<p class="MsoNormal" style="margin-left:0in;text-align:justify;text-indent:0in"><span lang="EN"><o:p>&nbsp;</o:p></span></p>

<p class="MsoNormal" style="margin-left:0in;text-align:justify;text-indent:0in"><b style="mso-bidi-font-weight:normal"><span lang="EN"><o:p>&nbsp;</o:p></span></b></p>

<p class="MsoNormal"><span lang="EN"><o:p>&nbsp;</o:p></span></p>

</div>




</body></html></h1>
        </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True, port=8000)


