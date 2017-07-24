/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

"use strict";

const {utils: Cu} = Components;
Cu.import("resource://gre/modules/XPCOMUtils.jsm");
Cu.import("resource://shield-recipe-client/lib/Sampling.jsm");
Cu.import("resource://shield-recipe-client/lib/PreferenceFilters.jsm");

XPCOMUtils.defineLazyModuleGetter(this, "mozjexl", "resource://shield-recipe-client/vendor/mozjexl.js");

this.EXPORTED_SYMBOLS = ["FilterExpressions"];

XPCOMUtils.defineLazyGetter(this, "jexl", () => {
  const jexl = new mozjexl.Jexl();
  jexl.addTransforms({
    date: dateString => new Date(dateString),
    stableSample: Sampling.stableSample,
    bucketSample: Sampling.bucketSample,
    preferenceValue: PreferenceFilters.preferenceValue,
    preferenceIsUserSet: PreferenceFilters.preferenceIsUserSet,
    preferenceExists: PreferenceFilters.preferenceExists,
    keys,
  });
  jexl.addBinaryOp("intersect", 40, operatorIntersect);
  return jexl;
});

this.FilterExpressions = {
  eval(expr, context = {}) {
    const onelineExpr = expr.replace(/[\t\n\r]/g, " ");
    return jexl.eval(onelineExpr, context);
  },
};

/**
 * Return an array of the given object's own keys (specifically, its enumerable
 * properties), or undefined if the argument isn't an object.
 * @param {Object} obj
 * @return {Array[String]|undefined}
 */
function keys(obj) {
  if (typeof obj !== "object" || obj === null) {
    return undefined;
  }

  return Object.keys(obj);
}

/**
 * Find all the values that are present in both lists. Returns undefined if
 * the arguments are not both Arrays.
 * @param {Array} listA
 * @param {Array} listB
 * @return {Array|undefined}
 */
function operatorIntersect(listA, listB) {
  if (!Array.isArray(listA) || !Array.isArray(listB)) {
    return undefined;
  }

  return listA.filter(item => listB.includes(item));
}
