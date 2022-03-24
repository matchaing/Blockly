Blockly.Blocks['takeoff'] = {
    init: function() {
        this.appendDummyInput()
            .appendField("take off");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(270);
        this.setTooltip("take off ");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['land'] = {
    init: function() {
        this.appendDummyInput()
            .appendField("land");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(270);
        this.setTooltip("land");
        this.setHelpUrl("");
    }
};