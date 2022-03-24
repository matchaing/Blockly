Blockly.Blocks['flight_move'] = {
    init: function() {
        this.appendDummyInput()
            .appendField("go")
            .appendField(new Blockly.FieldDropdown([["forward","forward"], ["backward","backward"], ["left","left"], ["right","right"]]), "direction")
            .appendField(new Blockly.FieldNumber(0, 20, 500, 1), "distance")
            .appendField("cm");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(240);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['up'] = {
    init: function() {
        this.appendDummyInput()
            .appendField("up")
            .appendField(new Blockly.FieldNumber(0, 20, 500), "NAME");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(240);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['down'] = {
    init: function() {
        this.appendDummyInput()
            .appendField("down")
            .appendField(new Blockly.FieldNumber(0, 20, 500), "NAME");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(240);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['ccw'] = {
    init: function() {
        this.appendDummyInput()
            .appendField("Rotate counterclockwise by")
            .appendField(new Blockly.FieldNumber(0, 1, 360), "angle")
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(240);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['cw'] = {
    init: function() {
        this.appendDummyInput()
            .appendField("Rotate clockwise by")
            .appendField(new Blockly.FieldNumber(0, 1, 360), "angle")
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(240);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['flip'] = {
    init: function() {
        this.appendDummyInput()
            .appendField("Flip")
            .appendField(new Blockly.FieldDropdown([["right","r"], ["left","l"], ["forward","f"], ["back","b"]]), "direction");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(240);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};