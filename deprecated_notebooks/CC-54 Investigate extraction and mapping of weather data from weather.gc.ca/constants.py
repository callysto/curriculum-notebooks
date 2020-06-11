HTML_CHECKBOX='''<html>
<body>
<p>Display some text when the checkbox is checked:</p>
Checkbox: <input type="checkbox" id="myCheck"  onclick="myFunction()">
<p id="text" style="display:block">Checkbox is CHECKED!</p>

<script>
function myFunction() {
    var checkBox = document.getElementById("myCheck");
    var text = document.getElementById("text");
    alert('Goodbye World!');
    if (checkBox.checked == true){
        text.style.display = "block";
        alert('Hello World!');
    } else {
       text.style.display = "none";
    }
}
</script>
</body>
</html>'''


HTML_POPUP='''<html>
<script type="text/Javascript">
    function set_table() {
        var var_station = document.getElementById('station').innerHTML;
        var var_index = document.getElementById('index').innerHTML;
        
        var command = "GLOBAL_SHOW_STATION = " + var_index;
        console.log("Executing Command: " + command);
        var kernel = IPython.notebook.kernel;
        kernel.execute(command);    
        }
        
</script>

<div>
<p id='station_name'>%s</p>
<p id='lat'>Latitude: %s<br>Longitude: %s</p>
<p id='index' hidden>%s</p>

<button type='button' onclick='set_table()'>Show in table</button>
</div>


</html>'''



input_form = """
<div style="background-color:gainsboro; border:solid black; width:300px; padding:20px;">
Variable Name: <input type="text" id="var_name" value="foo"><br>
Variable Value: <input type="text" id="var_value" value="bar"><br>
<button onclick="set_value()">Set Value</button>
</div>
"""

javascript = """
<script type="text/Javascript">
    function set_value(){
        var var_name = document.getElementById('var_name').value;
        var var_value = document.getElementById('var_value').value;
        var command = var_name + " = '" + var_value + "'";
        console.log("Executing Command: " + command);
        
        var kernel = IPython.notebook.kernel;
        kernel.execute(command);
    }
</script>
"""

HTML_TEMP = '''<html>
<script type="text/Javascript">
    function set_table() {
        var var_station = document.getElementById("station").innerHTML;
        var var_index = document.getElementById("index").innerHTML;
        
        var command = "GLOBAL_SHOW_STATION = " + var_index;
        console.log("Executing Command: " + command);
        var kernel = IPython.notebook.kernel;
        kernel.execute(command);    
        }
        
</script>

<div>
<p id='station_name'>%s</p>
<p id='lat'>Latitude: %s<br>Longitude: %s</p>
<p id='index' hidden>%s</p>

<button type='button' onclick='var var_station = document.getElementById("station_name").innerHTML; 
var var_index = document.getElementById("index").innerHTML; 
var command = "SET_GLOBAL_SHOW_STATION(" + var_index + ")"; 
console.log("Executing Command: " + command); 
var kernel = IPython.notebook.kernel; kernel.execute(command); 
comm = Jupyter.notebook.kernel.comm_manager.new_comm("_button_");
comm.send({"hello": "goodbye"});'>Show in table</button>
</div>


</html>'''


HTML_COMM = '''<html>
<div>
<p id='station_name'>%s</p>
<p id='lat'>Latitude: %s<br>Longitude: %s</p>
<p id='index'>%s</p>

<button type='button' onclick='var var_station = document.getElementById("station_name").innerHTML; 
var var_index = document.getElementById("index").innerHTML; 
var command = "SET_GLOBAL_SHOW_STATION(" + var_index + ")"; 
console.log("Executing Command: " + command); 
var kernel = IPython.notebook.kernel; kernel.execute(command); 
//comm = Jupyter.notebook.kernel.comm_manager.new_comm("_button_");
comm = Jupyter.notebook.kernel.comm_manager.new_comm("_table_callback_");
comm.send({"index": var_index});'>Show in table</button>
</div>


</html>'''



HTML_BUTTON='''<html>
<body>

<p id="show_in_table">no</p>
<button type="button" onclick="document.getElementById('show_in_table').innerHTML = 'yes'">Show in table</button>

</body>
</html>'''

OTHER = '''    comm = Jupyter.notebook.kernel.comm_manager.new_comm("_table_");
    comm.on_msg(function(msg) {
        if(msg['content']['data']['table'] != message)
        {
            message = msg['content']['data']['table'];
            console.log(message);
        }
    });
'''

HTML_TABLE = '''<html>
<head>

<!-- Let the user select the year and month of the data to display -->
<select id='_yearDateRange_' onchange='_setMonthRange_()'>
</select>
<select id='_monthDateRange_'>
</select>

<button type='button' onclick='_fetchStationData_()'>Update</button>

<style>
table {
    font-family: arial, sans-serif;
    border-collapse: collapse;
    width: 100;
}

td, th {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
}

tr:nth-child(even) {
    background-color: #dddddd;
}
</style>
<script>
// Global constant reference to the months
var _MONTHS_ = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
var _tableMessage_ = '';
//var _lastID_ = 0;
var _currentStationId = null;
var _tableComm_;
var _startMonth_ = 0;  // The first month data was recorded, indexed from 0
var _endMonth_ = 0;  // The last month data was recorded, indexed from 0

// Opens a comm to fetch the wether data of the selected year and month
function _fetchStationData_()
{
    console.log(_currentStationId_)
    if(_currentStationId_ != null)
    {
        var monthSelect = document.getElementById('_monthDateRange_');
        var yearSelect = document.getElementById('_yearDateRange_');
        var months = monthSelect.options;
        var years = yearSelect.options;
        var monthIndex = monthSelect.selectedIndex;
        var yearIndex = yearSelect.selectedIndex;

        // The currently selected month & year
        month = months[monthIndex].value;
        year = years[yearIndex].value;

        if (typeof month == 'undefined')
        {
            month = 0;
        }
        comm = Jupyter.notebook.kernel.comm_manager.new_comm('_table_callback_');
        comm.send({'index': _currentStationId_, 'year': year, 'month': month});
    }
}

// Removes all instances of a tag in an element
function _removeTag_(element, tag)
{
    // Tag names need to be in uppercase for compairison
    tag = tag.toUpperCase();
    var toRemove = [];
    var len = element.childNodes.length;
    for(var i = 0; i < len; ++i)
    {
        if(element.childNodes[i].tagName == tag)
        {
            element.removeChild(element.childNodes[i]);
            
            // List is now shorter
            len -= 1;
            i -= 1;
        }
    }
}

// Called whenever the year select changes to dynamically modify the
// month select
function _setMonthRange_(selectedMonth=0)
{
    var monthSelect = document.getElementById('_monthDateRange_');
    var yearSelect = document.getElementById('_yearDateRange_');
    //var value = monthSelect.value;
    var years = yearSelect.childNodes;
    var options = monthSelect.childNodes;
    var length = options.length;
    var start = 0;  // The first month
    var end = 12;  // The last month
    var index = yearSelect.selectedIndex;
    
    // If the selected year is the first or last, then it may not have
    // all of the months
    if(index == 0)
    {
        start = _startMonth_;
    }
    if(index == years.length-2)
    {
        end = _endMonth_;
    }

    // Allow index relative to the end with negative numbers
    if(selectedMonth < 0)
    {
        selectedMonth += end;
    }
    else
    {
        selectedMonth += start;
    }
    
    // Clear the month select
    _removeTag_(monthSelect, 'option')
    for(var i = start; i != end; ++i)
    {
        var option = document.createElement('option');
        var text = document.createTextNode(_MONTHS_[i]);
        option.appendChild(text);
        if(i == selectedMonth)
        {
            option.selected = 'selected';
        }
        option.value = i;
        monthSelect.appendChild(option);
    }
}

function _buildDropDown_(table)
{
    range = table['range'];
    yearDropDown = document.getElementById('_yearDateRange_');
    monthDropDown = document.getElementById('_monthDateRange_');
    
    // Remove all old instances of option
    _removeTag_(yearDropDown, 'OPTION');
    _removeTag_(monthDropDown, 'OPTION');
    
    // The first year
    i = range[0];  // The first year
    j = range[3];  // The last year
    for(i; i <= j; ++i)
    {
        var option = document.createElement('option');
        var text = document.createTextNode(i);
        option.appendChild(text);
        option.value = i;
        if(i == j)
        {
            option.selected = 'selected';
        }
        yearDropDown.appendChild(option);
    }
    
    // Save these values for later
    _startMonth_ = parseInt(range[1]);
    _endMonth_ = parseInt(range[4]);
    
    // Initialize the month select
    _setMonthRange_(-1);
}

function _tableCommCallback_(msg, id)
{
//    if(id != _lastID_)
//    {
    console.log(msg);
    _tableMessage_ = msg;
//    _lastID_ = id;
    _currentStationId_ = id;
    if(msg != null)
    {
        var table = document.getElementById('_weatherTable_');

        // Remove old elements
        var toRemove = [];
        var len = table.childNodes.length;
        for(var i = 0; i < len; ++i)
        {
            if(table.childNodes[i].tagName == 'TR')
            {
                table.removeChild(table.childNodes[i]);

                // Need to offset because the list is now shorter
                len -= 1;
                i -= 1;
            }
        }

        //
        document.getElementById('_tableHeader_').innerHTML = msg['date'];
        //console.log(msg['range']);
        _buildDropDown_(msg);

        var len = msg['day'].length;
        for(var i = 0; i < len; ++i)
        {
            // Make the row
            var row = document.createElement('tr');

            // Make each column
            var day  = document.createElement('td');
            var temp = document.createElement('td');
            var rain = document.createElement('td');
            var wind = document.createElement('td');

            // Changing null cells to have '-'
            if(msg['day'][i] == null)
            {
                msg['day'][i] = '-';
            }
            if(msg['temp'][i] == null)
            {
                msg['temp'][i] = '-';
            }   
            if(msg['rain'][i] == null)
            {
                msg['rain'][i] = '-';
            }    
            if(msg['wind'][i] == null)
            {
                msg['wind'][i] = '-';
            }

            // Add all the text
            var text = document.createTextNode(msg['day'][i]);
            day.appendChild(text);
            var text = document.createTextNode(msg['temp'][i]);
            temp.appendChild(text);
            var text = document.createTextNode(msg['rain'][i]);
            rain.appendChild(text);
            var text = document.createTextNode(msg['wind'][i]);
            wind.appendChild(text);

            row.appendChild(day);
            row.appendChild(temp);
            row.appendChild(rain);
            row.appendChild(wind);

            table.appendChild(row);
        }
    }
//    }
}

//function _registerTableComm_()
//{
//    _tableComm_ = Jupyter.notebook.kernel.comm_manager.new_comm("_table_");
//    _tableComm_.on_msg(function(msg)
//    {
//        _tableCommCallback_(msg['content']['data']['table'], msg['content']['data']['id']);
//    });
//}
//_registerTableComm_();

Jupyter.notebook.kernel.comm_manager.register_target('_table_',
    function(comm, msg) 
    {
        comm.on_msg(function(msg) 
        {
            _tableCommCallback_(msg['content']['data']['table'], msg['content']['data']['id']);
        });
        
        // Don't really need either of these
        //comm.on_close(function(msg) {...});
        //comm.send({'foo': 0});
    }
);

//window.setInterval(function commUpdate()
//{ 
//    console.log("Interval");
//    _registerTableComm_();
//    _tableComm_.send({});
//}, 100000);
</script>
</head>
<body>

<h2 id='_tableHeader_'>HTML Table</h2>

<table id='_weatherTable_'>
    <tr>
        <th>Day</th>
        <th>Mean Tempurature</th>
        <th>Total Presipitation</th>
        <th>Wind</th>
    </tr>
</table>
</body>
</html>'''


HTML_RANGE_SLIDER='''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>jQuery UI Slider - Range slider</title>
  <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
  <link rel="stylesheet" href="/resources/demos/style.css">
  <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
  <script>
  $( function() {
    $( "#slider-range" ).slider({
      range: true,
      min: 1840,
      max: 2018,
      values: [ 2000, 2003 ],
      slide: function( event, ui ) {
        $( "#amount" ).val( ui.values[ 0 ] + " - " + ui.values[ 1 ] );
      }
    });
    $( "#amount" ).val( "$" + $( "#slider-range" ).slider( "values", 0 ) +
      " - $" + $( "#slider-range" ).slider( "values", 1 ) );
  } );
  </script>
</head>
<body>
 
<p>
  <label for="amount">Year range:</label>
  <input type="text" id="amount" readonly style="border:0; color:#f6931f; font-weight:bold;">
</p>
 
<div id="slider-range"></div>
 
 
</body>
</html>'''


NO_UI_SLIDER='''
<html>
<body>
<script>
var range = document.getElementById('range');

nouislider/nouislider.create(range, {

	range: {
		'min': 1300,
		'max': 3250
	},

	step: 150,

	// Handles start at ...
	start: [ 1450, 2050, 2350, 3000 ],

	// ... must be at least 300 apart
	margin: 300,

	// ... but no more than 600
	limit: 600,

	// Display colored bars between handles
	connect: true,

	// Put '0' at the bottom of the slider
	direction: 'rtl',
	orientation: 'vertical',

	// Move handle on tap, bars are draggable
	behaviour: 'tap-drag',
	tooltips: true,
	format: wNumb({
		decimals: 0
	}),

	// Show a scale with the slider
	pips: {
		mode: 'steps',
		stepped: true,
		density: 4
	}
});
</script>

<p id="range"></p>

</body>
</html>'''


HTML_SLIDER='''<!DOCTYPE html>
<html>
<body>

<h1>Custom Range Slider</h1>
<p>Drag the slider to display the current value.</p>

<div class="slidecontainer">
  <input type="range" min="1840" max="2018" value="2000" class="slider" id="myRange" oninput='document.getElementById("demo").innnerHTML=document.getElementById("myRange").value;'>
  <p>Value: <span id="demo"></span></p>
</div>

</body>
</html>'''