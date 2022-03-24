Blockly.JavaScript['take_off'] = function(block) {
    var value_alt = Blockly.JavaScript.valueToCode(block, 'ALT', Blockly.JavaScript.ORDER_ATOMIC);
    var checkbox_wait = block.getFieldValue('WAIT') == 'TRUE';
    // TODO: Assemble JavaScript into code variable.
    var code = 'window.alert("take off");';
    return code;
  };

//   Blockly.Python.take_off = function(block) {
// 	simpleOffboard();

// 	let z = Blockly.Python.valueToCode(block, 'ALT', Blockly.Python.ORDER_NONE);

// 	if (block.getFieldValue('WAIT') == 'TRUE') {
// 		rosDefinitions.navigateWait = true;
// 		simpleOffboard();

// 		return `navigate_wait(z=${z}, frame_id='body', auto_arm=True)\n`;
// 	} else {
// 		return `navigate(z=${z}, frame_id='body', auto_arm=True)\n`;
// 	}
// }