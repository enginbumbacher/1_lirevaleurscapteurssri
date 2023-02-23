datalogger.deleteLog()
datalogger.mirrorToSerial(true)
basic.forever(function () {
    datalogger.includeTimestamp(FlashLogTimeStampFormat.Seconds)
    datalogger.mirrorToSerial(true)
    datalogger.log(datalogger.createCV("Light", input.lightLevel()))
})
