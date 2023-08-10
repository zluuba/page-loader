#!/usr/bin/env node
import { Command } from 'commander';
import downloadPage from '../src/core.js';

const program = new Command();

program
  .name('page-loader')
  .description('Page loader utility')
  .version('0.1.0')
  .helpOption('-h, --help', 'display help for command')
  .argument('<url>')
  .option('-o, --output [dir]', 'output dir', process.cwd())
  .action((url, options) => downloadPage(url, options.output)
    .then((pageName) => console.log(pageName))
    .catch((error) => {
      console.error(`Oops. ${error.message}`);
      process.exit(1);
    }));

program.parse();
