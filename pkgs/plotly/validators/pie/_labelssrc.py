import _plotly_utils.basevalidators


class LabelssrcValidator(_plotly_utils.basevalidators.SrcValidator):

    def __init__(self, plotly_name='labelssrc', parent_name='pie', **kwargs):
        super(LabelssrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'none'),
            role=kwargs.pop('role', 'info'),
            **kwargs
        )
