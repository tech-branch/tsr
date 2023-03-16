## Low-overhead time recorder

Least invasive, csv based, linear time recorder that doesn't keep your data hostage. 

This tool uses a simple two-column format for storing a record

```
datetime,tags delimited by space
```

Each record should mark a newly started activity, that way context switches are much more consious.

The tag has a default value of 'next' to minimise the time required to operate the tool, you can edit the records manually later 

A file can consist entirely of "next" rows if you so wish, making the tool minimally invasive to your productivity (albeit a bit more difficult to read):

```
<Opt+Space> 'tsr' <Enter>
```

Adding new activities with tags is also quite simple

```
<Opt+Space> tsr <Tab> slack request <Enter>
<Opt+Space> tsr <Tab> migration client <Enter>
<Opt+Space> tsr <Tab> lunch <Enter>
<Opt+Space> tsr <Tab> incident interrupted 2431 <Enter>
<Opt+Space> tsr <Tab> work eod <Enter>
```

Based on the output, you can create custom reports and do your visualisation wizardry
