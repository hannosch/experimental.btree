
def initialize(context):
    import setpatches
    setpatches.apply()

    # The set patches are only temporary
    # to avoid zc.relationship trying to persist
    # the BTree functions
    setpatches.unapply()
