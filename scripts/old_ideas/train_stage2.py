
modelName = 'scratch'

args = {}
args['outputDir'] = '/home3/skaasyap/willett/neural_seq_decoder/output/' + modelName
args['datasetPath'] = '/home3/skaasyap/willett/data'
args['seqLen'] = 150
args['maxTimeSeriesLen'] = 1200
args['batchSize'] = 24
args['lrStart'] = 0.02
args['lrEnd'] = 0.02
args['nUnits'] = 1024
args['nBatch'] = 30000 #3000
args['nLayers'] = 5
args['seed'] = 0
args['nClasses'] = 40
args['nInputFeatures'] = 256
args['dropout'] = 0.4
args['whiteNoiseSD'] = 0.8
args['constantOffsetSD'] = 0.2
args['gaussianSmoothWidth'] = 2.0
args['strideLen'] = 4
args['kernelLen'] = 32
args['bidirectional'] = False
args['l2_decay'] = 1e-5
args['device'] = 'cuda:1'

args['latentspeech_dim_stage2'] = 1024
args['nLayers_stage2'] = 1
args['dropout_stage2'] = 0.4
args['nUnits_stage2'] = 256
args['bidirectional_stage2'] = True
args['l2_decay_stage2'] = 1e-5
args['dropout_stage2'] = 0.4
args['outputdim_stage2'] = 256
args['strideLen_stage2'] = 1
args['kernelLen_stage2'] = 4
args["bucket_size"] = 8000 # half a second of data (audio is in 16Khz)
args["min_samples_in_bucket"] = 8


from neural_decoder.speech2neural import trainModel

trainModel(args)