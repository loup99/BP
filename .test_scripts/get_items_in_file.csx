#r "nuget: PGCG.commonItems, 5.3.0"

using commonItems;
using System;
using System.IO;

string filePath = Args[0];

var keysToOutput = new List<string>();

var parser = new Parser();
parser.RegisterRegex(CommonRegexes.Catchall, (reader, key) => {
    keysToOutput.Add(key);
    ParserHelpers.IgnoreItem(reader);
});

parser.ParseFile(filePath);

Console.WriteLine(string.Join(" ", keysToOutput));