import _plotly_utils.basevalidators


class LineValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='line', parent_name='scattergl', **kwargs):
        super(LineValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop('data_class_str', 'Line'),
            data_docs=kwargs.pop(
                'data_docs', """
            color
                Sets the line color.
            dash
                Sets the style of the lines.
            shape
                Determines the line shape. The values
                correspond to step-wise line shapes.
            width
                Sets the line width (in px).
"""
            ),
            **kwargs
        )
