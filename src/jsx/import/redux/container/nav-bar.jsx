/**
 * nav-bar.jsx: redux store for navigation bar.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
 *
 */

import React from 'react';
import { connect } from 'react-redux';
import NavBar from '../../navigation/nav-bar.jsx';
import { setResultsButton } from '../action/page.jsx';

// wraps each function of the object to be dispatch callable
const mapDispatchToProps = (dispatch) => {
    return {
        dispatchResultsButton: dispatch.bind(setResultsButton)
    }
}

// pass selected properties from redux state tree to component
const NavBarState = connect(
    null,
    mapDispatchToProps
)(NavBar)

// indicate which class can be exported, and instantiated via 'require'
export default NavBarState
