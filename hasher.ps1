<# 
    .Author
        Paul McDowell
    .License
        MIT
    .Description
        The following script simplifies producing a hash from a string of text.
        Just load the string you want into the first parameter, then specify the 
        supported hashing mode with the second parameter. See Get-FileHash help 
        documentation for a list of available hashes under the -Algorithm parameter.
#>
param(
    [Parameter()]
    [string]$textString,
    
    [Parameter()]
    [string]$hashType
)


$hashStream = [System.IO.MemoryStream]::new()
$writer = [System.IO.StreamWriter]::new($hashStream)
$writer.Write($textString)
$writer.Flush()
$hashStream.Position = 0
Write-Host $(Get-FileHash -InputStream $hashStream -Algorithm $hashType)