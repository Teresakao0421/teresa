
//% account=0 color=#3CB371 icon="\uf0ad" block="Tools"
namespace tools {
    /**
    * 連網路
    */
    //% blockId="wifi" block="number of wifi account %account|passwords %passwords"
    //% blockGap=2 account=0 
    export function wifi(account: number, passwords:number): void {
        basic.showNumber(account*passwords)
    }
    /**
    