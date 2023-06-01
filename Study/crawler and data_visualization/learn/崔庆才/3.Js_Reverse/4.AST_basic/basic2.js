import { parse } from "@babel/parser";
import generate from "@babel/generator"
import traverse from "@babel/traverse";
import * as types from "@babel/types";
import fs from "fs";


// // 利用AST修改、删除源码
// const code = fs.readFileSync("code1.js", "utf-8");
// let ast = parse(code);
// traverse(ast, {
//     NumericLiteral(path) {
//         if (path.node.value == 3) {
//             path.node.value = 5;
//         }
//     },
//     StringLiteral(path) {
//         if (path.node.value == "hello") {
//             path.node.value = "hi";
//         }
//     },
//     CallExpression(path) {
//         if (path.node.callee.object.name === "console" && path.node.callee.property.name === "log") {
//             path.remove();
//         }
//     },
// });
// const {code: output} = generate(ast, {
//     retainLines: true,
// });
// console.log(output);


// 利用AST增加代码
const code = "const a = 1;";
let ast = parse(code);
traverse(ast, {
    VariableDeclaration(path) {
        let init = types.binaryExpression("+", types.identifier("a"), types.numericLiteral(1));
        let declarator = types.variableDeclarator(types.identifier("b"), init);
        let declaration= types.variableDeclaration("const", [declarator]);
        path.insertAfter(declaration);
        path.stop();
    },
});
const output = generate(ast, {
    retainLines: true,
}).code;
console.log(output);