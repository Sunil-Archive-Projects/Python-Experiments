//pahntomJS script
//takes two arguments (link,pdfTitle) and renders the page into PDF

var system=require('system');
var page = require('webpage').create();

var args=system.args;
page.viewportSize = {
  width: 1600,
  height: 900
};//set the window height width

link=args[1];
pdfTitle=args[2];

if(args.length == 3)
{
  page.open(link, function(status) //open the page
  {
    console.log("Status: " + status);
    if(status === "success") 
    {
      page.render(pdfTitle+'.pdf',{'format':'pdf','quality':'100'});
    }
    phantom.exit();
  });
}
else
{
  console.log("Invalid Number of arguments!!");
  phantom.exit();
}