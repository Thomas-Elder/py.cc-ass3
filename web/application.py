import lift

application = lift.create_application()

if __name__ == "__main__":
    application.debug = True
    application.run()