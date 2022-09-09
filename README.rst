Grid Layout widgets for trame
==================================

trame-grid-layout extend trame **widgets** with components that can be used to create some dynamic grid layout containers.
It leverage [vue-grid-layout](https://github.com/jbaysolutions/vue-grid-layout) which is a grid layout system, like 
[Gridster](http://dsmorse.github.io/gridster.js/), for Vue.js. Heavily inspired by [React-Grid-Layout](https://github.com/react-grid-layout/react-grid-layout).


Installing
-----------------------------------------------------------

trame-grid-layout can be installed with `pip <https://pypi.org/project/trame-grid-layout/>`_:

.. code-block:: bash

    pip install --upgrade trame-grid-layout


Usage
-----------------------------------------------------------

The `Trame Tutorial <https://kitware.github.io/trame/docs/tutorial.html>`_ is the place to go to learn how to use the library and start building your own application.

The `API Reference <https://trame.readthedocs.io/en/latest/index.html>`_ documentation provides API-level documentation.


License
-----------------------------------------------------------

trame-grid-layout is made available under the MIT License License. For more details, see `LICENSE <https://github.com/Kitware/trame-grid-layout/blob/master/LICENSE>`_
This license has been chosen to match the one use by `vue-grid-layout <https://github.com/react-grid-layout/react-grid-layout/blob/master/LICENSE>`_ which can be exposed via this library.


Community
-----------------------------------------------------------

`Trame <https://kitware.github.io/trame/>`_ | `Discussions <https://github.com/Kitware/trame/discussions>`_ | `Issues <https://github.com/Kitware/trame/issues>`_ | `RoadMap <https://github.com/Kitware/trame/projects/1>`_ | `Contact Us <https://www.kitware.com/contact-us/>`_

.. image:: https://zenodo.org/badge/410108340.svg
    :target: https://zenodo.org/badge/latestdoi/410108340


Enjoying trame?
-----------------------------------------------------------

Share your experience `with a testimonial <https://github.com/Kitware/trame/issues/18>`_ or `with a brand approval <https://github.com/Kitware/trame/issues/19>`_.


Development: Grabbing client before push to PyPI
-----------------------------------------------------------

To update the client code, run the following command line while updating the targeted version

.. code-block:: console

    mkdir -p ./trame_grid_layout/module/serve
    curl https://unpkg.com/vue-grid-layout@2.4.0 -Lo ./trame_grid_layout/module/serve/vue-grid-layout.js

Simple example
-----------------------------------------------------------

.. code-block:: python

    from trame.app import get_server
    from trame.ui.vuetify import SinglePageLayout
    from trame.widgets import vuetify, grid

    server = get_server()
    state = server.state

    LAYOUT = [
        {"x": 0, "y": 0, "w": 2, "h": 2, "i": "0"},
        {"x": 2, "y": 0, "w": 2, "h": 4, "i": "1"},
        {"x": 4, "y": 0, "w": 2, "h": 5, "i": "2"},
        {"x": 6, "y": 0, "w": 2, "h": 3, "i": "3"},
        {"x": 8, "y": 0, "w": 2, "h": 3, "i": "4"},
        {"x": 10, "y": 0, "w": 2, "h": 3, "i": "5"},
        {"x": 0, "y": 5, "w": 2, "h": 5, "i": "6"},
        {"x": 2, "y": 5, "w": 2, "h": 5, "i": "7"},
        {"x": 4, "y": 5, "w": 2, "h": 5, "i": "8"},
        {"x": 6, "y": 3, "w": 2, "h": 4, "i": "9"},
        {"x": 8, "y": 4, "w": 2, "h": 4, "i": "10"},
        {"x": 10, "y": 4, "w": 2, "h": 4, "i": "11"},
        {"x": 0, "y": 10, "w": 2, "h": 5, "i": "12"},
        {"x": 2, "y": 10, "w": 2, "h": 5, "i": "13"},
        {"x": 4, "y": 8, "w": 2, "h": 4, "i": "14"},
        {"x": 6, "y": 8, "w": 2, "h": 4, "i": "15"},
        {"x": 8, "y": 10, "w": 2, "h": 5, "i": "16"},
        {"x": 10, "y": 4, "w": 2, "h": 2, "i": "17"},
        {"x": 0, "y": 9, "w": 2, "h": 3, "i": "18"},
        {"x": 2, "y": 6, "w": 2, "h": 2, "i": "19"},
    ]

    with SinglePageLayout(server) as layout:
        layout.title.set_text("Grid layout")
        with layout.content:
            with grid.GridLayout(
                layout=("layout", LAYOUT),
                row_height=20,
            ):
                grid.GridItem(
                    "{{ item.i }}",
                    v_for="item in layout",
                    key="item.i",
                    v_bind="item",
                    classes="pa-4",
                    style="border: solid 1px #333; background: rgba(128, 128, 128, 0.5);",
                )

    if __name__ == "__main__":
        server.start()
