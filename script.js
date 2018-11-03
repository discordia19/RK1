'use strict';

const fs = require('fs');
const RK = require('./RK.js');
const BraunRobinson = require('./BraunRobinson.js');
const AnaliticsMethod = require('./AnaliticsMethod').AnaliticsMethod;

const fileVariant = fs.readFileSync('variant.json', 'utf-8');
const variant = JSON.parse(fileVariant).matrix;
const testVariant = [
    [2, 1, 3],
    [3, 0, 1],
    [1, 2, 1]
];

const rk = new RK();
console.log(`Итоговая цена игры: ${rk.getGameCost()}`);

// const an = new AnaliticsMethod(testVariant);
// an.showGameResults();

// const br = new BraunRobinson(testVariant);
// console.log(br.getGameCost());
// br.startGameConsole();