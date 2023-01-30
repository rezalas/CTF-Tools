<# 
    .Author
        Paul McDowell
    .License
        MIT
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