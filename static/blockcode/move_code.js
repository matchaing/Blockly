Blockly.JavaScript['flight_move'] = function(block) {
    var dropdown_direction = block.getFieldValue('direction');
    var number_distance = block.getFieldValue('distance');
    
    // TODO: Assemble JavaScript into code variable.
    switch(dropdown_direction){
        case forward:
            var code = '...;\n';
            break;
        case backward:
            var code = '...;\n';
            break;
        case left:
            var code = '...;\n';
            break;
        case right:
            var code = '...;\n';
            break;
        default:
            var code = '...;\n';
    }
    return code;
};

Blockly.JavaScript['up'] = function(block) {
    var number_name = block.getFieldValue('NAME');
    // TODO: Assemble Python into code variable.
    var code = 'print('+number_name+')';
    return code;
};

Blockly.JavaScript['down'] = function(block) {
var number_name = block.getFieldValue('NAME');
// TODO: Assemble JavaScript into code variable.
var code = '...;\n';
return code;
}

Blockly.JavaScript['rotation_ccw'] = function(block) {
    var number_angle = block.getFieldValue('angle');
    // TODO: Assemble JavaScript into code variable.
    var code = 'window.alert('+number_angle+');';
    return code;
};

Blockly.JavaScript['rotation_cw'] = function(block) {
var number_angle = block.getFieldValue('angle');
// TODO: Assemble JavaScript into code variable.
var code = 'window.alert('+number_angle+');';
return code;
};

Blockly.JavaScript['flip'] = function(block) {
    var dropdown_direction = block.getFieldValue('direction');
    // TODO: Assemble JavaScript into code variable.
    var code = '...;\n';
    return code;
};