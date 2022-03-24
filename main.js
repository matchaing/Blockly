// // window.runProgram = function() {
// // 	if (ros.params.confirm_run && !confirm('Run program?')) return;

// // 	runRequest = true;
// // 	update();
// // 	var code = generateCode(workspace);
// // 	console.log(code);
// // 	ros.runService.callService(new ROSLIB.ServiceRequest({ code: code } ), function(res) {
// // 		if (!res.success) {
// // 			runRequest = false;
// // 			update();
// // 			alert(res.message);
// // 		}
// // 	}, function(err) {
// // 		runRequest = false;
// // 		update();
// // 		alert(err);
// // 	})
// // }

// function runProgrming(event) {
//     var code = Blockly.JavaScript.workspaceToCode(workspace);
//     document.getElementById('textarea').value = code;
//   }
//   workspace.addChangeListener(myUpdateFunction);

var workspace = Blockly.inject('blocklyDiv', {toolbox: document.getElementById('toolbox')});

function onFirstComment(event) {
    if (event.type == Blockly.Events.BLOCK_CHANGE &&
        event.element == 'comment' &&
        !event.oldValue && event.newValue) {
      alert('Congratulations on creating your first comment!')
      workspace.removeChangeListener(onFirstComment);
    }
  }
  workspace.addChangeListener(onFirstComment);