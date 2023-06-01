import { parse } from "@babel/parser";  // 将js代码解析为AST
import generate from "@babel/generator";  // 将AST还原成js代码
import fs from "fs";


const code = fs.readFileSync("code1.js", "utf-8");
let ast = parse(code);

// 打印AST
// console.log(ast);
// 打印body内容
// console.log(ast.program.body);

//还原js代码
const {code: output} = generate(ast);
console.log(output);