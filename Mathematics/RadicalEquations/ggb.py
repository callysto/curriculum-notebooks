from IPython.display import display, HTML, Javascript

# This package provides a bunch of python functions to wrap Geogebra's API.
# The basic idea is to create three tiers of objects:
#   - The top level GGB object stores global configuration options and
#       generates Blueprint objects from .ggb files, material ids, or base64.
#   - Each Blueprint object stores all the configuration options necessary
#       to render a Geogebra applet as a Drawing object. The same Blueprint
#       may be used to render multiple copies of the same drawing.
#   - Each Drawing object corresponds to geogebra applet that has been
#       rendered onto the page and contains all the methods necessary to
#       make api calls on that specific rendering.


# The GGBOptions class contains settings that are shared by all three objects.
class GGBOptions():
    def __init__(self):
        self.params = dict()
        self.paramsList = []
        self.paramsString = ''
        return

    # Just some getter methods.
    def asDict(self):
        return self.params

    def asList(self):
        self.paramsList = list(map(
            lambda kv: '\"%s\" : %s' % (kv[0], kv[1]),
            self.params.items()
        ))
        return self.paramsList

    def asString(self):
        self.paramsList = list(map(
            lambda kv: '\"%s\": %s' % (kv[0], kv[1]),
            self.params.items()
        ))
        self.paramsString = ', '.join(self.paramsList)
        return self.paramsString

    # A few crudely made typechecking methods. It's likely this will change.
    @staticmethod
    def isStringType(key):
        return key in [
            'appName',
            'width',
            'height',
            'material_id',
            'filename',
            'ggBase64',
            'borderColor',
            'customToolbar',
            'perspective',
            'algebraInputPosition',
            'scaleContainerClass',
            'rounding',
            'language',
            'country',
            'ggbOnInitParam',
            'data-param-id'
        ]

    @staticmethod
    def isNumberType(key):
        return key in [
            'width',
            'height',
            'capturingThreshold',
            'scale',
            'showAnimationButton',
            'showFullscreenButton',
            'showSuggestionButtons',
            'showStartTooltip',
            'butonShadows',
            'buttonRounding'
        ]

    @staticmethod
    def isBoolType(key):
        return key in [
            'enableRightClick',
            'enableLabelDrags',
            'enableShiftDragZoom',
            'errorDialogsActive',
            'showMenuBar',
            'showToolBar',
            'showToolBarHelp',
            'showAlgebraInput',
            'showResetIcon',
            'allowStyleBar',
            'useBrowserForJS',
            'showLogging',
            'enableFileFeatures',
            'enable3d',
            'enableCAS',
            'preventFocus',
            'allowUpscale',
            'playButton'
        ]


# The GGB class initializes the javascript requirements, generates Blueprints,
# and sets global defaults.
class GGB(GGBOptions):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.blueprintDB = dict()
        self.lastBlueprint = ''

        ggbRequire = ('''
            require.config({
                paths: {
                    ggb: "https://cdn.geogebra.org/apps/deployggb"
                }
            });

            require(["ggb"]);
        ''')
        display(Javascript(ggbRequire))
        return

    # A helper method for the file, material, base64, and app methods.
    def src(self, source: str, type: str, instanceName=''):
        if instanceName is '':
            self.lastBlueprint = 'ggb_' + str(self.counter)
            self.counter += 1
        else:
            self.lastBlueprint = 'ggb_' + instanceName

        self.blueprintDB[self.lastBlueprint] = GGBBlueprint(source, type=type, instanceName=self.lastBlueprint, params=super().asDict().copy())
        return self.blueprintDB[self.lastBlueprint]

    # Generates a Blueprint object from a .ggb file.
    def file(self, filename: str, instanceName=''):
        return self.src(filename, 'filename', instanceName)

    # Generates a Blueprint object from a material id.
    def material(self, material_id: str, instanceName=''):
        return self.src(material_id, 'material_id', instanceName)

    # Generates a Blueprint object from a base64 string.
    def base64(self, code: str, instanceName=''):
        return self.src(code, 'ggbBase64', instanceName)

    # Generates a Blueprint object for a standard app.
    def app(self, name='classic', instanceName=''):
        return self.src(name, 'appName', instanceName)

    # A helper method for setting global default options.
    def setOption(self, name: str, value):
        self.params[name] = value
        return self

    # A general method that accepts a sequence of key=value pairs and uses them
    # to set global default options. Once these are set then all Blueprints
    # generated will also have those options. Useful when inserting lots of
    # applets with the same settings.
    def setDefaultOptions(self, **kwargs):
        if kwargs is not None:
            for key, val in kwargs.items():
                if GGBOptions.isNumberType(key):
                    self.setOption(key, val)
                elif GGBOptions.isBoolType(key):
                    self.setOption(key, str(val).lower())
                else:
                    self.setOption(key, '\"%s\"' % val)
        return self

    # Just a dummy method to suppress output on Jupyter cells without the
    # need of a semicolon.
    def _ipython_display_(self):
        return

    # A static method for grabbing the value of a JavaScript variable and
    # putting it into a Python variable. Very primitive, do not use.
    @staticmethod
    def getJSVar(pVarName: str, jsVarName: str):
        display(Javascript('IPython.notebook.kernel.execute("%s=" + %s)' % (pVarName, jsVarName)))
        return


# The Blueprint class contains settings and information needed to generate
# instances of a geogebra applet to the page (by generating Drawing objects).
# The same Blueprint can be used to render many copies of the same applet.
class GGBBlueprint(GGBOptions):
    def __init__(self, source: str, type: str, instanceName: str, params):
        super().__init__()
        self.params = params
        self.instanceName = instanceName
        self.counter = 0
        self.drawingDB = dict()
        self.lastDrawing = ''

        self.params[type] = '\"%s\"' % source
        return

    # A helper method for setting options for the Blueprint.
    def setOption(self, name: str, value):
        self.params[name] = value
        return self

    # A convenience method for setting the width option.
    def width(self, width: int):
        self.setOption('width', width)
        return self

    # A convenience method for setting the height option.
    def height(self, height: int):
        self.setOption('height', height)
        return self

    # A general method that accepts a sequence of key=value pairs and uses them
    # to set Blueprint options. Once these are set then all Drawings generated
    # will also have those options. Useful when rendering lots of copies of
    # the same applet with the same settings.
    def options(self, **kwargs):
        if kwargs is not None:
            for key, val in kwargs.items():
                if GGBOptions.isNumberType(key):
                    self.setOption(key, val)
                elif GGBOptions.isBoolType(key):
                    self.setOption(key, str(val).lower())
                else:
                    self.setOption(key, '\"%s\"' % val)
        return self

    # The method that generates a Drawing from the Blueprint.
    def draw(self):
        self.lastDrawing = self.instanceName + '_' + str(self.counter) + 'e'
        self.counter += 1

        self.drawingDB[self.lastDrawing] = GGBDrawing(super().asDict().copy(), self.lastDrawing)

        return self.drawingDB[self.lastDrawing]

    # Just a dummy method to suppress output on Jupyter cells without the
    # need of a semicolon.
    def _ipython_display_(self):
        return


# The Drawing class that corresponds to a rendered applet on the page.
# Each Drawing contains methods for making api calls to that rendered applet.
class GGBDrawing(GGBOptions):
    def __init__(self, params, instanceName):
        super().__init__()
        self.params = params
        self.instanceName = instanceName

        display(HTML('<div id=\"%s\"></div>' % self.instanceName))

        display(Javascript(
            'var %s = new GGBApplet({%s}, \"%s\", false); %s.inject(); ' % (self.instanceName, super().asString(), self.instanceName, self.instanceName)
        ))
        return

    # Just a dummy method to suppress output on Jupyter cells without the
    # need of a semicolon.
    def _ipython_display_(self):
        return

    # Convenience method and proof of concept that sets an object in a
    # Geogebra render to either visible or invisible.
    def setVisible(self, obj, tf):
        display(Javascript('%s.setVisible(\"%s\", %s)' % (self.instanceName, obj, str(tf).lower())))
        return self

    # A method for making setter-style API calls that don't return anything.
    def set(self, fn: str, *args):
        test = GGBApi.isSetterShort(fn)
        if test is not False:
            fn = test
        if GGBApi.isSetter(fn):
            jsArgs = []
            # Don't use isinstance() to avoid bool as a subtype of int
            for arg in args:
                if type(arg) is int or type(arg) is float:
                    jsArgs.append(str(arg))
                elif type(arg) is bool:
                    jsArgs.append(str(arg).lower())
                else:
                    jsArgs.append('\"%s\"' % arg)
            jsArgsString = ', '.join(jsArgs)

            display(Javascript('%s.%s(%s)' % (self.instanceName, fn, jsArgsString)))
        return self

    # A method for making getter-style API calls that assign the returned Value
    # to the python variable with name pVarName (as a string).
    def get(self, pVarName: str, fn: str, *args):
        test = GGBApi.isGetterShort(fn)
        if test is not False:
            fn = test
        if GGBApi.isGetter(fn):
            jsArgs = []
            # Don't use isinstance() to avoid bool as a subtype of int
            for arg in args:
                if type(arg) is int or type(arg) is float:
                    jsArgs.append(str(arg))
                elif type(arg) is bool:
                    jsArgs.append(str(arg).lower())
                else:
                    jsArgs.append('\"%s\"' % arg)
            jsArgsString = ', '.join(jsArgs)
            display(Javascript(
                'var tempVarOut = "";\n' + 'var tempVar = %s.%s(%s);' % (self.instanceName, fn, jsArgsString) + '''
                if (typeof(tempVar) === "number") {
                    tempVarOut = tempVar;
                } else if (typeof(tempVar) === "boolean") {
                    tempVarOut = tempVar ? 'True' : 'False';
                } else if (typeof(tempVar) === "string") {
                    tempVarOut = '"' + tempVar + '"';
                } else if (Array.isArray(tempVar)) {
                    tempVarOut = '[' + tempVar.toString() + ']';
                }
                ''' + 'console.log(tempVarOut); IPython.notebook.kernel.execute("%s=" + tempVarOut);' % pVarName)
            )
        return self


# Just a helper class that sanity checks some API calls. It's likely this will
# change. The plan is to refactor this so that it actually generates a Python
# method for each API call from some basic string data.
class GGBApi():
    def __init__(self):
        return

    @staticmethod
    def isSetter(fn):
        return fn in [
            'deleteObject',
            'setAuxiliary',
            'setCaption',
            'setColor',
            'setVisible',
            'setLabelVisible',
            'setLabelStyle',
            'setCoords',
            'setValue',
            'setTextValue',
            'setListValue',
            'setFixed',
            'setTrace',
            'setLayer',
            'setLayerVisible',
            'setLineStyle',
            'setLineThickness',
            'setPointStyle',
            'setPointSize',
            'setDisplayStyle',
            'setFilling',
            'setAnimating',
            'setAnimationSpeed',
            'startAnimation',
            'stopAnimation',
            'setMode',
            'reset',
            'newConstruction',
            'refreshViews',
            'setOnTheFlyPointCreationActive',
            'setPointCapture',
            'setRounding',
            'hideCursorWhenDragging',
            'setRepaintingActive',
            'setErrorDialogsActive',
            'setCoordSystem',
            'setAxesVisible',
            'setAxesVisible',
            'setAxisLabels',
            'setAxisSteps',
            'setAxisUnits',
            'setGridVisible',
            'undo',
            'redo',
            'showToolBar',
            'setCustomToolBar',
            'showMenuBar',
            'showAlgebraInput',
            'showResetIcon',
            'enableRightClick',
            'enableLabelDrags',
            'enableShiftDragZoom',
            'enableCAS',
            'enable3D',
            'setPerspective',
            'setWidth',
            'setHeight',
            'setSize',
            'recalculateEnvironments'
        ]

    # Short aliases for the setter methods.
    @staticmethod
    def isSetterShort(fn):
        short = {
            'Auxiliary': 'setAuxiliary',
            'Caption': 'setCaption',
            'Color': 'setColor',
            'Visible': 'setVisible',
            'LabelVisible': 'setLabelVisible',
            'LabelStyle': 'setLabelStyle',
            'Coords': 'setCoords',
            'Value': 'setValue',
            'TextValue': 'setTextValue',
            'ListValue': 'setListValue',
            'Fixed': 'setFixed',
            'Trace': 'setTrace',
            'Layer': 'setLayer',
            'LayerVisible': 'setLayerVisible',
            'LineStyle': 'setLineStyle',
            'LineThickness': 'setLineThickness',
            'PointStyle': 'setPointStyle',
            'PointSize': 'setPointSize',
            'DisplayStyle': 'setDisplayStyle',
            'Filling': 'setFilling',
            'Animating': 'setAnimating',
            'AnimationSpeed': 'setAnimationSpeed',
            'Mode': 'setMode',
            'OnTheFlyPointCreationActive': 'setOnTheFlyPointCreationActive',
            'PointCapture': 'setPointCapture',
            'Rounding': 'setRounding',
            'RepaintingActive': 'setRepaintingActive',
            'ErrorDialogsActive': 'setErrorDialogsActive',
            'CoordSystem': 'setCoordSystem',
            'AxesVisible': 'setAxesVisible',
            'AxisLabels': 'setAxisLabels',
            'AxisSteps': 'setAxisSteps',
            'AxisUnits': 'setAxisUnits',
            'GridVisible': 'setGridVisible',
            'CustomToolBar': 'setCustomToolBar',
            'Perspective': 'setPerspective',
            'Width': 'setWidth',
            'Height': 'setHeight',
            'Size': 'setSize'
        }
        if fn in short:
            return short[fn]
        else:
            return False

    @staticmethod
    def isGetter(fn):
        return fn in [
            'renameObject',
            'getPNGBase64',
            'writePNGtoFile',
            'isIndependent',
            'isMoveable',
            'isAnimationRunning',
            'getXcoord',
            'getYcoord',
            'getZcoord',
            'getValue',
            'getListValue',
            'getColor',
            'getVisible',
            'getValueString',
            'getDefinitionString',
            'getCommandString',
            'getLaTeXString',
            'getLaTeXBase64',
            'getObjectType',
            'exists',
            'isDefined',
            'getObjectNumber',
            'getCASObjectNumber',
            'getObjectName',
            'getLayer',
            'getLineStyle',
            'getLineThickness',
            'getPointStyle',
            'getPointSize',
            'getFilling',
            'getCaption',
            'getLabelStyle',
            'getLabelVisible',
            'getMode',
            'getGridVisible',
            'getPerspectiveXML'
        ]

    # Short aliases for the getter methods.
    @staticmethod
    def isGetterShort(fn):
        short = {
            'PNGBase64': 'getPNGBase64',
            'Xcoord': 'getXcoord',
            'Ycoord': 'getYcoord',
            'Zcoord': 'getZcoord',
            'Value': 'getValue',
            'ListValue': 'getListValue',
            'Color': 'getColor',
            'Visible': 'getVisible',
            'ValueString': 'getValueString',
            'DefinitionString': 'getDefinitionString',
            'CommandString': 'getCommandString',
            'LaTeXString': 'getLaTeXString',
            'LaTeXBase64': 'getLaTeXBase64',
            'ObjectType': 'getObjectType',
            'ObjectNumber': 'getObjectNumber',
            'CASObjectNumber': 'getCASObjectNumber',
            'ObjectName': 'getObjectName',
            'Layer': 'getLayer',
            'LineStyle': 'getLineStyle',
            'LineThickness': 'getLineThickness',
            'PointStyle': 'getPointStyle',
            'PointSize': 'getPointSize',
            'Filling': 'getFilling',
            'Caption': 'getCaption',
            'LabelStyle': 'getLabelStyle',
            'LabelVisible': 'getLabelVisible',
            'Mode': 'getMode',
            'GridVisible': 'getGridVisible',
            'PerspectiveXML': 'getPerspectiveXML'
        }
        if fn in short:
            return short[fn]
        else:
            return False
