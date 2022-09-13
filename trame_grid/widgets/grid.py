from trame_client.widgets.core import AbstractElement
from .. import module, update_layout


class HtmlElement(AbstractElement):
    def __init__(self, _elem_name, children=None, **kwargs):
        super().__init__(_elem_name, children, **kwargs)
        if self.server:
            self.server.enable_module(module)


class GridLayout(HtmlElement):
    def __init__(self, children=None, layout_updated=None, **kwargs):
        """
        `GridLayout <https://jbaysolutions.github.io/vue-grid-layout/guide/properties.html#gridlayout>`_

        :param layout: The value must be an Array of Object items. Each item must have i, x, y, w and h properties. Please refer to the documentation for GridItem below for more information.
        :param responsive_layouts: This is the initial layouts of the grid per breakpoint if responsive is set to true. The keys of the Object are breakpoint names and each value is an Array of Object items as defined by layout prop. eg:{ lg:[layout items], md:[layout items] }. Setting the prop after the creation of the GridLayout has no effect. See also responsive, breakpoints and cols.
        :param col_num: (default: 12) Says how many columns the grid has. The value should be a natural number.
        :param row_height: (default: 150) Says what is a height of a single row in pixels.
        :param max_rows: (default: Infinity) Says what is a maximal number of rows in the grid.
        :param margin: (default: [10, 10]) Says what are the margins of elements inside the grid. The value must be a two-element Array of Number. Each value is expressed in pixels. The first element is a margin horizontally, the second element is a vertical margin.
        :param is_draggable: (default: True) Says if the grids items are draggable.
        :param is_resizable: (default: True) Says if the grids items are resizable.
        :param is_mirrored: (default: False) Says if the RTL/LTR should be reversed.
        :param is_bounded: (default: False) Says if the grid items are bounded to the container when dragging
        :param auto_size: (default: True) Says if the container height should swells and contracts to fit contents.
        :param vertical_compact: (default: True) Says if the layout should be compact vertically.
        :param restore_on_drag: (default: False) Says if the moved grid items should be restored after an item has been dragged over.
        :param prevent_collision: (default: False) Says if grid items will move when being dragged over.
        :param use_css_transforms: (default: True) Says if the CSS transition-property: transform; should be used.
        :param responsive: (default: False) Says if the layout should be responsive to window width. See also responsiveLayouts, breakpoints and cols.
        :param breakpoints: (default: "{ lg: 1200, md: 996, sm: 768, xs: 480, xxs: 0 }")  Breakpoints defined for responsive layout, the parameter represents the width of different devices:lg(large), md(medium), sm(small), xs(extra small). Sets widths on which column number changes. See also responsiveLayouts and cols.
        :param cols: (default: "{ lg: 12, md: 10, sm: 6, xs: 4, xxs: 2 }") Defines number of columns for each breakpoint
        :param use_style_cursor: (default: True) Says if set the styleCursor option to true. When dragging freezes, setting this value to false may alleviate problems. This property is not reactive.
        :param transform_scale: (default: 1) Sets a scaling factor to the size of the grid items, 1 is 100%

        Events

        :param layout_created: Emitted on the component created lifecycle hook
        :param layout_before_mount: Emitted on the component beforeMount lifecycle hook
        :param layout_mounted: Emitted on the component mounted lifecycle hook
        :param layout_ready: Emitted when all the operations on the mount hook finish
        :param layout_updated: Every time the layout has finished updating and positions of all grid-items are recalculated
        :param breakpoint_changed: Every time the breakpoint value changes due to window resize

        """
        if layout_updated is None:
            layout_updated = (self.update, "[$event]")

        super().__init__(
            "grid-layout",
            children,
            layout_updated=layout_updated,
            **kwargs,
        )
        self._attr_names += [
            ("layout", ":layout"),
            ("layout_sync", ":layout.sync"),
            ("responsive_layouts", "responsiveLayouts"),
            ("col_num", ":colNum"),
            ("row_height", ":rowHeight"),
            ("max_rows", ":maxRows"),
            ("margin", ":margin"),
            ("is_draggable", "isDraggable"),
            ("is_resizable", "isResizable"),
            ("is_mirrored", "isMirrored"),
            ("is_bounded", "isBounded"),
            ("auto_size", "autoSize"),
            ("vertical_compact", "verticalCompact"),
            ("restore_on_drag", "restoreOnDrag"),
            ("prevent_collision", "preventCollision"),
            ("use_css_transforms", "useCssTransforms"),
            ("responsive"),
            ("breakpoints"),
            ("cols"),
            ("use_style_cursor", "useStyleCursor"),
            ("transform_scale", "transformScale"),
        ]
        self._event_names += [
            ("layout_created", "layout-created"),
            ("layout_before_mount", "layout-before-mount"),
            ("layout_mounted", "layout-mounted"),
            ("layout_ready", "layout-ready"),
            ("layout_updated", "layout-updated"),
            ("breakpoint_changed", "breakpoint-changed"),
        ]
        self._layout_name = kwargs.get("layout", kwargs.get("layout_sync"))
        if isinstance(self._layout_name, (tuple, list)):
            self._layout_name = self._layout_name[0]

    def update(self, new_layout):
        if self._layout_name:
            update_layout(self._server.state[self._layout_name], new_layout)


class GridItem(HtmlElement):
    def __init__(self, children=None, **kwargs):
        """
        `GridItem <https://jbaysolutions.github.io/vue-grid-layout/guide/properties.html#griditem>`_


        :param i:
        :param x:
        :param y:
        :param w:
        :param h:
        :param min_w:
        :param min_h:
        :param max_w:
        :param max_h:
        :param is_draggable:
        :param is_resizable:
        :param is_bounded:
        :param static:
        :param drag_ignore_from:
        :param drag_allow_from:
        :param resize_ignore_from:
        :param preserve_aspect_ratio:
        :param drag_option:
        :param resize_option:

        Events

        :param move: Every time an item is being moved and changes position.

            .. code-block:: javascript

                function moveEvent(i, newX, newY){
                    console.log("MOVE i=" + i + ", X=" + newX + ", Y=" + newY);
                }

        :param resize: Every time an item is being resized and changes size

            .. code-block:: javascript

                resizeEvent: function(i, newH, newW, newHPx, newWPx){
                    console.log("RESIZE i=" + i + ", H=" + newH + ", W=" + newW + ", H(px)=" + newHPx + ", W(px)=" + newWPx);
                }

        :param resized: Every time an item is finished being resized and changes size

            .. code-block:: javascript

                /**
                 *
                 * @param i the item id/index
                 * @param newH new height in grid rows
                 * @param newW new width in grid columns
                 * @param newHPx new height in pixels
                 * @param newWPx new width in pixels
                 *
                 */
                resizedEvent: function(i, newH, newW, newHPx, newWPx){
                    console.log("RESIZED i=" + i + ", H=" + newH + ", W=" + newW + ", H(px)=" + newHPx + ", W(px)=" + newWPx);
                }

        :param container_resized: Every time the grid item/layout container changes size (browser window or other)

            .. code-block:: javascript

                /**
                 *
                 * @param i the item id/index
                 * @param newH new height in grid rows
                 * @param newW new width in grid columns
                 * @param newHPx new height in pixels
                 * @param newWPx new width in pixels
                 *
                 */
                containerResizedEvent: function(i, newH, newW, newHPx, newWPx){
                    console.log("CONTAINER RESIZED i=" + i + ", H=" + newH + ", W=" + newW + ", H(px)=" + newHPx + ", W(px)=" + newWPx);
                },

        :param moved: Every time an item is finished being moved and changes position

            .. code-block:: javascript

                movedEvent: function(i, newX, newY){
                    console.log("MOVED i=" + i + ", X=" + newX + ", Y=" + newY);
                }
        """
        super().__init__(
            "grid-item",
            children,
            **kwargs,
        )
        self._attr_names += [
            "i",
            "x",
            "y",
            "w",
            "h",
            ("min_w", "minW"),
            ("min_h", "minH"),
            ("max_w", "maxW"),
            ("max_h", "maxH"),
            ("is_draggable", "isDraggable"),
            ("is_resizable", "isResizable"),
            ("is_bounded", "isBounded"),
            "static",
            ("drag_ignore_from", "dragIgnoreFrom"),
            ("drag_allow_from", "dragAllowFrom"),
            ("resize_ignore_from", "resizeIgnoreFrom"),
            ("preserve_aspect_ratio", "preserveAspectRatio"),
            ("drag_option", "dragOption"),
            ("resize_option", "resizeOption"),
        ]
        self._event_names += [
            ("resize", "resize"),
            ("move", "move"),
            ("resized", "resized"),
            ("container_resized", "container-resized"),
            ("moved", "moved"),
        ]
