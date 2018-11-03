const BraunRobinson = require('./BraunRobinson');

class RK {
    constructor() {
        this.a = -4;
        this.b = 10 / 3;
        this.c = 16 / 3;
        this.d = -16 / 30;
        this.e = -112 / 30;
        this.N = 20;
        this.matrix = undefined;
    }

    getH(x, y) {
        return this.a * x * x + this.b * y * y + this.c * x * y + this.d * x + this.e * y;
    }

    findCurrentCost() {
        let len = this.matrix.length;
        for (let row = 0; row < this.matrix.length; row++) {
            let minElement = this.matrix[row][0];
            let minElementPos = 0;
            for (let col = 0; col < len; col++) {
                if (this.matrix[row][col] < minElement) {
                    minElement = this.matrix[row][col];
                    minElementPos = col;
                }
            }
            for (let curRow = 0; curRow < len; curRow++) {
                if (minElement <= this.matrix[curRow][minElementPos] && (curRow != row)) {
                    break;
                }

                if (curRow == this.matrix.length - 1) {
                    console.log('седловая точка найдена ' + minElement);
                    return minElement;
                    // return { minElement, row, minElementPos }; // седловая точка, и ее координаты.
                }
            }
        }

        console.log('седловая точка не найдена!')
        const br = new BraunRobinson(this.matrix);
        return br.getGameCost();
    }

    initMatrix(rows, cols) {
        this.matrix = [];
        for (let i = 0; i < rows; i++) {
            this.matrix.push([]);
            for (let j = 0; j < cols; j++) {
                this.matrix[i].push(this.getH(i / this.N, j / this.N));
            }
        }

        // console.log(this.matrix);
    }

    getGameCost() {
        return this.gameCost ? this.gameCost : this.calculateGameCost();
    }

    calculateGameCost() {
        let maxCost;
        for (let i = 1; i < this.N; i++) {
            this.initMatrix(i, i); // starting 1,1
            //return 1;
            if (i == 1) {
                maxCost = this.matrix[0][0];
                this.gameCost = maxCost;
                console.log(`Первая седловая точка: ${maxCost}`);
                continue;
            }

            if (this.findCurrentCost() > maxCost) {
                this.gameCost = maxCost;
                // break;
            }
        }

        return this.gameCost;
    }
}

module.exports = RK;