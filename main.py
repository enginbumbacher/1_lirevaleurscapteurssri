datalogger.delete_log()
datalogger.mirror_to_serial(True)

def on_forever():
    datalogger.include_timestamp(FlashLogTimeStampFormat.SECONDS)
    datalogger.mirror_to_serial(True)
    datalogger.log(datalogger.create_cv("Light", input.light_level()))
basic.forever(on_forever)
