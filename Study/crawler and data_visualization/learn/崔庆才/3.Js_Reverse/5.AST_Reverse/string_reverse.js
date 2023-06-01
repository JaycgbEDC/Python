import { parse } from "@babel/parser";
import generate from "@babel/generator";
import traverse from "@babel/traverse";
import * as types from "@babel/types";
import fs from "fs";


const code = 'const strings = ["\x68\x65\x6c\x6c\x6f", "\x77\x6f\x72\x6c\x64"];';
let ast = parse(code);

traverse(ast, {
    StringLiteral({ node }) {
        if (node.extra && /\\[ux]/gi.test(node.extra.raw)) {
            node.extra.raw = node.extra.rawvalue;
        }
    },
});

const { code: output } = generate(ast);
console.log(output);