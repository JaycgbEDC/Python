import { parse } from "@babel/parser";
import generate from "@babel/generator";
import traverse from "@babel/traverse";
import * as types from "@babel/types";
import fs from "fs";


const code = fs.readFileSync("code2.js", "utf-8");
let ast = parse(code);

traverse(ast, {
    IfStatement(path) {
        let {consequent, alternate} = path.node;
        let testPath = path.get("test");
        const evaluateTest = testPath.evaluateTruthy();
        if (evaluateTest === true) {
            if (types.isBlockStatement(consequent)) {
                consequent = consequent.body;
            }
            path.replaceWithMultiple(consequent);
        } else if (evaluateTest === false) {
            if (alternate != null) {
                if (types.isBlockStatement(alternate)) {
                    alternate = alternate.body;
                }
                path.replaceWithMultiple(alternate);
            } else {
                path.remove()
            }
        }
    },
});

const { code: output } = generate(ast);
console.log(output);