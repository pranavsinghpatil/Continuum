export interface Task {
    id: string;
    name: string;
    status: 'PENDING' | 'RUNNING' | 'COMPLETED' | 'FAILED';
}

export interface Workflow {
    id: string;
    protocolName: string;
    tasks: Task[];
    status: 'INITIALIZED' | 'RUNNING' | 'COMPLETED';
}

export interface Artifact {
    id: string;
    name: string;
    path: string;
    metadata?: Record<string, any>;
}

export interface TXF {
    version: number;
    taskId: string;
    role: string;
    capability: string;
    context: Record<string, any>;
    prompt: string;
}

export interface ExecutionProvider {
    submit(taskId: string, txfPayload: TXF): string;
    status(taskId: string): string;
}

export interface Organization {
    name: string;
    version: string;
    roles: any[];
}

export interface Knowledge {
    id: string;
    content: string;
}

export interface Protocol {
    name: string;
    steps: any[];
}

export interface Capability {
    name: string;
    description: string;
}
