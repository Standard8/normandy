import PropTypes from 'prop-types';
import React from 'react';
import { connect } from 'react-redux';

import * as recipeActions from 'control_new/state/recipes/actions';

@connect(
  null,
  {
    fetchRecipeHistory: recipeActions.fetchRecipeHistory,
  },
)
export default class QueryRecipeHistory extends React.Component {
  static propTypes = {
    fetchRecipeHistory: PropTypes.func.isRequired,
    pk: PropTypes.number.isRequired,
  }

  componentWillMount() {
    const { fetchRecipeHistory, pk } = this.props;
    fetchRecipeHistory(pk);
  }

  componentWillReceiveProps(nextProps) {
    const { fetchRecipeHistory, pk } = this.props;
    if (pk !== nextProps.pk) {
      fetchRecipeHistory(nextProps.pk);
    }
  }

  render() {
    return null;
  }
}
