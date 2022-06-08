import _plotly_utils.basevalidators


class CminValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self,
        plotly_name='cmin',
        parent_name='sankey.link.concentrationscales',
        **kwargs
    ):
        super(CminValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'calc'),
            role=kwargs.pop('role', 'info'),
            **kwargs
        )
