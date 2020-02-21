# DNDBot by VGFreak95


## DNDBot Main class commands:
>**roll_dice**(*ctx*, *amount*, *dice_type*)   <br />
**Purpose**: Rolls Dice.   <br />

**Parameters**:   <br />
*ctx* -> context    <br />
*amount* -> amount of dice you would like to roll (ex: 3)   <br />
*dice_type* -> the sided dice you would like to roll (ex: 20 for d20)

___
___


>**roll_character**(*ctx*, *first*, *last*)   <br />
**Purpose**: Rolls random character for you.   <br />

**Parameters**:   <br />
*ctx* -> context    <br />
*first* -> first name of the character you would like to create  <br />
*last* -> last name of the character you would like to create

___
___


>**del_char**(*ctx*, *first*, *last*)   <br />
**Purpose**: Deletes character that *you* have created.        <br />

**Parameters**:   <br />
*ctx* -> context    <br />
*first* -> first name of the character you would like to delete  <br />
*last* -> last name of the character you would like to delete

___
___


>**swap_values**(*ctx*, *first*, *last*, *att1*, *att2*)   <br />
**Purpose**: Swaps atrributes of the character.       <br />

**Parameters**:   <br />
*ctx* -> context    <br />
*first* -> first name of the character you would like to modify  <br />
*last* -> last name of the character you would like to modify <br/>
*att1* -> the attribute you would like to swap for the other attribute (att2) <br />
*att2* -> the attribute you would like to swap for the other attribute (att1) <br/>

___
___


>**reroll_char**(*ctx*, *first*, *last*, *att1*, *att2*)   <br />
**Purpose**: Rerolls 2 values of your choice.      <br />

**Parameters**:   <br />
*ctx* -> context    <br />
*first* -> first name of the character you would like to reroll  <br />
*last* -> last name of the character you would like to reroll <br/>
*att1* -> the attribute you would like to reroll <br />
*att2* -> the attribute you would like to reroll  <br/>

___
___

>**stats**(*ctx*, *first*, *last*)   <br />
**Purpose**: Shows the stats of the player selected   <br />

**Parameters**:   <br />
*ctx* -> context    <br />
*first* -> first name of the character you would like to check  <br />
*last* -> last name of the character you would like to check


___
___
___
___
___


## Bot Controller Class Commands:

>**shutdown**(*self*, *ctx*)   <br />
**Purpose**: Shutdowns the bot via messaging in the discord server     <br />

**Parameters**:   <br />
*self* -> self <br/>
*ctx* -> context <br/>


___
___


>**restart**(*self*, *ctx*)   <br />
**Purpose**: Restarts the discord bot via messaging in the discord server    <br />

**Parameters**:   <br />
*self* -> self <br/>
*ctx* -> context
