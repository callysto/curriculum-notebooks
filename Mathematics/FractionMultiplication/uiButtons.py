#Custom magic functions, to use call 'import uiButtons' in a cell
#once the library has been imported magic commands may be used
#eg. %uiButtons

from __future__ import print_function
from IPython.core.magic import Magics, magics_class, line_magic
from IPython import get_ipython

@magics_class
class MyMagics(Magics):

    #When run it initilizes the 'show/hide code' buttons and the 'initialize' button
    @line_magic
    def uiButtons(self, line):
        raw_code = '''%%html
                    <script>
                    document.getElementById('toggleButton').onclick = function () {
                        if (code_shown) {
                            $('div.input').hide('500');
                            $('#toggleButton').val('Show Code')
                        } else {
                            $('div.input').show('500');
                            $('#toggleButton').val('Hide Code')
                        }
                        code_shown = !code_shown
                    }

                    document.getElementById('init').onclick = function () {
                        runAll = document.getElementById('run_all_cells_below').childNodes[1]
                        console.log(runAll)
                        runAll.click()
                    }

                    $(document).ready(function () {
                        code_shown = true;
                        $('div.input').hide()
                    });
                </script>
                <input type="submit" id="toggleButton" value="Show Code">
                <input id="init" type="submit" value="Initialize">'''

        self.shell.run_cell(raw_code, store_history=False)

#define more custom magic function here as needed.

ip = get_ipython()
ip.register_magics(MyMagics)