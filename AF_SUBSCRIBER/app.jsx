// Create a new window panel
var windowPanel = new Window("palette", "Compositions and Layers");
windowPanel.orientation = "row";
windowPanel.alignChildren = "left";

  #include "json2.jsx"

payload_data = []

fs.mkdirSync("directory", 0766, function(err){
  if(err){
     alert(err);
      // echo the result back
      
  }
});
 
// Function to populate the window panel with compositions and layers
function populateWindowPanel() {
  var compositions = app.project.items;
  
  for (var i = 1; i <= compositions.length; i++) {
    if (compositions[i] instanceof CompItem) {
      var composition = compositions[i];
      var compositionGroup = windowPanel.add("group");
      compositionGroup.orientation = "column";
     
      var layerNameText = compositionGroup.add("statictext", undefined, composition.name);
      layerNameText.alignment = "left";
      layerNameText.spacing = 50;
      layerNameText.size = [150, 25];
      
      layerNameText.enabled = true;
      layerNameText.textSize = 25;
      layerNameText.graphics.font = ScriptUI.newFont(layerNameText.graphics.font.name, ScriptUI.FontStyle.BOLD, 35); 
      layerNameText.graphics.foregroundColor = layerNameText.graphics.newPen(layerNameText.graphics.PenType.SOLID_COLOR, [1, 0, 0], 1);
       
      
      
      //compositionCheckbox.onClick = toggleComposition;
      layerNameText.composition = composition;
      for (var j = 1; j <= composition.layers.length; j++) {
        var layer = composition.layers[j];
        compositionGroup.orientation = "column";       
        var layerCheckbox = compositionGroup.add("checkbox", undefined, layer.name);
       
        layerCheckbox.alignment = "left";
        layerCheckbox.onClick = toggleLayer;
        layerCheckbox.layer = layer;
        layerCheckbox.value = true; // Select the checkbox
         
        layerCheckbox.composition = composition.name
         
      }
    }
  }
}

// Toggle composition visibility based on checkbox state
function toggleComposition() {
  var composition = this.composition;
  composition.enabled = this.value;
  for (var i = 1; i <= composition.layers.length; i++) {
    var layer = composition.layers[i];
    layer.enabled = this.value;
  }
}
compositionData = [] 
// Toggle layer visibility based on checkbox state
function toggleLayer() {
  var layer = this.layer;  
  layer.enabled = this.value;



  
}

// Populate the window panel with compositions and layers
populateWindowPanel();


 

var sendButton = windowPanel.add("button", undefined, "Save");



function sendData(filepath, path){


 
 
  var curlCommand = 'curl -X get http://localhost:8000/new?file='+filepath+'&path='+path+'   -H "Accept: application/json"  -H "Content-Type:Content-Type: application/json"'
  
  
  var result = system.callSystem(curlCommand);
  
 
}


sendButton.onClick = function() {
     
  var compositionData = [];
  
  // Iterate through all compositions in the project
  for (var i = 1; i <= app.project.numItems; i++) {
    var item = app.project.item(i);

    // Check if the item is a composition
    if (item instanceof CompItem) {
      var composition = item;
      var compositionInfo = {
        compositionName: composition.name,
        compwidth: composition.width,
        compHeight:composition.height,
        layers: []
      };

      // Iterate through all layers in the composition
      for (var j = 1; j <= composition.layers.length; j++) {
        var layer = composition.layers[j];

        // Check if the layer is a text layer or an image layer
        if (layer instanceof TextLayer || layer instanceof AVLayer) {
          var layerInfo = {
            layerName: layer.name,
            layerType: layer instanceof TextLayer ? "Text" : "Image",
            properties: {}
          };

          // Add text property
          if (layer instanceof TextLayer) {
            var textProperties = layer.property("Source Text");
            layerInfo.properties.text = textProperties.value.text;
            layerInfo.properties.position=[layer.property("Position").value[0], layer.property("Position").value[1]];
            layerInfo.properties.width=layer.width;
            layerInfo.properties.height= layer.height;
            layerInfo.properties.scale=layer.scale.value;
            layerInfo.properties.color=textProperties.value.fillColor
            layerInfo.properties.size=textProperties.value.fontSize   }

          // Add image property
          if (layer instanceof AVLayer) {
            if (layer.source instanceof FootageItem && layer.source.file) {
              layerInfo.properties.imageFilePath = layer.source.file.fsName;
              layerInfo.properties.position=[layer.property("Position").value[0], layer.property("Position").value[1]];
                layerInfo.properties.width=layer.width;
                layerInfo.properties.height= layer.height;
                layerInfo.properties.scale=layer.scale.value;
            }
          }

          // Add the layer info to the composition info
          compositionInfo.layers.push(layerInfo);
        }
      }

      // Add the composition info to the composition data
      compositionData.push(compositionInfo);

    }





  

  }


  var jsonData = JSON.stringify(compositionData );

  
 
  var projectFile = app.project.file;
    var projectName = null;
    var projectPath = null
     
    if (projectFile) {
    var fileName = projectFile.name;
    projectName = fileName.substring(0, fileName.lastIndexOf('.'));
    projectPath = projectFile.fsName;
    }

  // Specify the absolute file path
  var filePath =  projectName+".json";
   
  
  var file = new File('C:\\aftemp\\'+filePath);
  file.open("w");
  file.write(jsonData);
  file.close();
  var projectFile = app.project.file; 
  alert("All lyers  sent to server successfully .");
  sendData(projectName, 'C:\\aftemp')
  
}
// Show the window panel
windowPanel.show();
