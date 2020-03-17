import cwlgen

cwl_workflow = cwlgen.Workflow('', label='', doc='', cwl_version='v1.0')

#print("*** cwlgen ***")
#print(dir(cwlgen))

#print("*** workflow ***")
#print(dir(cwl_workflow))

# add scatter requirement to workflow
cwl_workflow.requirements.append(cwlgen.ScatterFeatureRequirement())

# add multiple inputs requirement to workflow
cwl_workflow.requirements.append(cwlgen.MultipleInputFeatureRequirement())

# add inputs
input = cwlgen.InputParameter('message_array', param_type='string[]')
cwl_workflow.inputs.append(input)

# add outputs
output = cwlgen.WorkflowOutputParameter('output', output_source='cat_2/output', param_type='File')
cwl_workflow.outputs.append(output)

# add step 1 (echo)
step1 = cwlgen.WorkflowStep('echo', run='1st-tool.cwl', scatter='message')

#print(dir(step1))

# add inputs to step1
step1_input = cwlgen.WorkflowStepInput('message', source='message_array')
step1.inputs.append(step1_input)

# add outputs to step1
step1_output = cwlgen.WorkflowStepOutput('echo_out')
step1.out.append(step1_output)




# add step 2 (cat)
step2 = cwlgen.WorkflowStep('cat', run='./cat.cwl')

# add inputs to step2
step2_input = cwlgen.WorkflowStepInput('files', source='echo/echo_out')
step2.inputs.append(step2_input)

# add outputs to step2
step2_output = cwlgen.WorkflowStepOutput('output')
step2.out.append(step2_output)



# add step3 (1st_tool)
step3 = cwlgen.WorkflowStep('1st_tool', run='./1st-tool.cwl', scatter='message')

# add inputs to step3
step3_input = cwlgen.WorkflowStepInput('message', source='message_array')
step3.inputs.append(step3_input)

# add outputs to step3
step3_output = cwlgen.WorkflowStepOutput('echo_out')
step3.out.append(step3_output)



# add step4 (cat_1)
step4 = cwlgen.WorkflowStep('cat_1', run='./cat.cwl')

# add inputs to step4
step4_input = cwlgen.WorkflowStepInput('files', source='1st_tool/echo_out')
step4.inputs.append(step4_input)

# add outputs to step4
step4_output = cwlgen.WorkflowStepOutput('output')
step4.out.append(step4_output)



# add step5 (cat_2)
step5 = cwlgen.WorkflowStep('cat_2', run='./cat.cwl')

# add inputs to step5
step5_input = cwlgen.WorkflowStepInput('files', source=['cat/output', 'cat_1/output'])
step5.inputs.append(step5_input)

# add outputs to step5
step5_output = cwlgen.WorkflowStepOutput('output')
step5.out.append(step5_output)



# add steps to workflow
cwl_workflow.steps.append(step1)
cwl_workflow.steps.append(step2)
cwl_workflow.steps.append(step3)
cwl_workflow.steps.append(step4)
cwl_workflow.steps.append(step5)


cwl_workflow.export()
